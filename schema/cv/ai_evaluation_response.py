from openai import BaseModel


class AIEvaluationResponse(BaseModel):
    evaluation: str