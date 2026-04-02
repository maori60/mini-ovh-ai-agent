import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def fallback_analysis(customer_request: str) -> dict:
    request = customer_request.lower()

    needs: list[str] = []
    solutions: list[str] = []

    if "scalable" in request or "scale" in request:
        needs.append("scalability")
        solutions.append("Public Cloud")

    if "secure" in request or "security" in request:
        needs.append("security")
        solutions.append("Private Network")

    if "storage" in request or "data" in request or "backup" in request:
        needs.append("storage")
        solutions.append("Object Storage")

    if "high traffic" in request or "traffic" in request:
        needs.append("availability")
        solutions.append("Load Balancer")

    if not needs:
        needs = ["general infrastructure"]
        solutions = ["Virtual Machines"]

    return {
        "needs": needs,
        "suggested_solutions": solutions,
        "justification": "Fallback analysis based on keyword detection.",
        "next_step": "Clarify requirements with the client.",
    }


def analyze_with_ai(customer_request: str) -> str:
    try:
        prompt = f"""
You are a cloud solutions architect.

Analyze the customer request and return a valid JSON object with exactly these keys:
- needs
- suggested_solutions
- justification
- next_step

Rules:
- "needs" must be a list of strings
- "suggested_solutions" must be a list of strings
- "justification" must be a string
- "next_step" must be a string
- Return JSON only
- Do not add markdown
- Do not add explanations outside the JSON

Customer request:
{customer_request}
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        content = response.choices[0].message.content

        if not content:
            fallback = fallback_analysis(customer_request)
            return json.dumps(fallback)

        return content

    except Exception:
        fallback = fallback_analysis(customer_request)
        return json.dumps(fallback)