from fastapi import FastAPI

from moodi.api import story_check, story_gen, summation
from moodi.utils.config import load_config

load_config("config/dev.env")

app = FastAPI()

# API 라우터 추가
app.include_router(
    story_gen.router, prefix="/gemini", tags=["Story Generation"]
)

app.include_router(story_check.router, prefix="/gemini", tags=["Story Check"])

app.include_router(summation.router, prefix="/local", tags=["Summation"])
