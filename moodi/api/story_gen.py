from fastapi import APIRouter, HTTPException

from moodi.models.schemas import ErrorResponse, StoryRequest, StoryResponse
from moodi.prompts.story_gen import get_story_response

router = APIRouter()


@router.post(
    "/story_gen",
    response_model=StoryResponse,
    responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}},
)
async def generate_story(request: StoryRequest):
    try:
        response = get_story_response(request)
        return response

    except ValueError as ve:
        raise HTTPException(
            status_code=400,
            detail={"error": "Invalid request payload", "message": str(ve)},
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Internal server error",
                "message": "스토리를 생성하는 중 문제가 발생했습니다.",
            },
        )
