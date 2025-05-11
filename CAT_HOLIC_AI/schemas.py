from pydantic import BaseModel
from typing import List

class StoryRequest(BaseModel):
    age: int
    social_situation: str
    learning_history_summary: str

class StoryResponse(BaseModel):
    story: str
    question: str
    choices: List[str]
    correct_answer: str

class ErrorResponse(BaseModel):
    error: str
    message: str
