from pydantic import BaseModel
from typing import List

# story-gen
class StoryRequest(BaseModel):
    age: int
    social_situation: str
    learning_history_summary: str

class StoryResponse(BaseModel):
    story: str
    question: str
    choices: List[str]
    correct_answer: str

# story-check
class StoryCheckRequest(BaseModel):
    story: str
    question: str
    choices: List[str]
    correct_answer: str
    user_selected: str

class StoryCheckResponse(BaseModel):
    correct_answer: str
    user_selected: str
    explanation: str

# summation
class RecentAnswer(BaseModel):
    story: str
    question: str
    user_selected: str
    correct_answer: str

class SummationRequest(BaseModel):
    recent_answers: List[RecentAnswer]

class SummationResponse(BaseModel):
    learning_history_summary: str

# 공통 에러
class ErrorResponse(BaseModel):
    error: str
    message: str
