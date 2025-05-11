from fastapi import FastAPI, HTTPException
from langchain_google_genai import ChatGoogleGenerativeAI
from CAT_HOLIC_AI.utils import get_gemini_api_key, load_config
from CAT_HOLIC_AI.schemas import StoryRequest, StoryResponse, ErrorResponse
from CAT_HOLIC_AI.prompts import story_prompt, output_parser

# 환경변수 로딩
load_config(env_path="config/dev.env")

app = FastAPI()

chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=get_gemini_api_key()
)

@app.post("/generate-story", response_model=StoryResponse, responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}})
async def generate_story(request: StoryRequest):
    try:
        prompt = story_prompt.format(
            age=request.age,
            social_situation=request.social_situation,
            learning_history_summary=request.learning_history_summary
        )

        response = chat_model.invoke(prompt)
        parsed_response = output_parser.parse(response.content)

        return StoryResponse(**parsed_response)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail={
            "error": "Invalid request payload",
            "message": str(ve)
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "error": "Internal server error",
            "message": "스토리를 생성하는 중 문제가 발생했습니다."
        })
