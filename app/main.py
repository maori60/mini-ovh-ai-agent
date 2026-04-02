from fastapi import FastAPI, HTTPException
from app.schemas import AnalyzeRequest, AnalyzeResponse
import json
app = FastAPI(title="Mini OVH AI Agent")


def detect_needs(customer_request: str) -> tuple[list[str], list[str], str, str]:
    text = customer_request.lower()

    needs: list[str] = []
    suggested_solutions: list[str] = []

    if "scalable" in text or "scalability" in text:
        needs.append("scalability")
        suggested_solutions.append("Public Cloud")

    if "available" in text or "availability" in text or "resilience" in text:
        needs.append("availability")
        suggested_solutions.append("Load Balancer")

    if "storage" in text or "backup" in text or "data" in text:
        needs.append("storage")
        suggested_solutions.append("Object Storage")

    if "secure" in text or "security" in text:
        needs.append("security")
        suggested_solutions.append("Private Network")

    if not needs:
        needs.append("general infrastructure")
        suggested_solutions.append("Public Cloud")

    justification = (
        "Suggested solutions were selected based on keywords detected in the customer request."
    )
    next_step = "Clarify traffic, budget, security constraints, and storage needs."

    return needs, suggested_solutions, justification, next_step


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Mini OVH AI Agent is running"}


from app.services.ai_service import analyze_with_ai
import json

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    try:
        ai_response = analyze_with_ai(request.customer_request)
        data = json.loads(ai_response)
        return AnalyzeResponse(**data)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI analysis failed: {str(e)}"
        )