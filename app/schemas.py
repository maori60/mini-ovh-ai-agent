from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    customer_request: str = Field(..., min_length=5)


class AnalyzeResponse(BaseModel):
    needs: list[str]
    suggested_solutions: list[str]
    justification: str
    next_step: str