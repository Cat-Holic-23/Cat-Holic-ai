from fastapi import APIRouter, HTTPException

from moodi.models.schemas import (
    ErrorResponse,
    StoryCheckRequest,
    StoryCheckResponse,
)
from moodi.prompts.story_check import get_story_check_response

router = APIRouter()


@router.post(
    "/story-check",
    response_model=StoryCheckResponse,
    responses={
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
        503: {"model": ErrorResponse},
    },
)
async def check_story(request: StoryCheckRequest):
    if request.user_selected not in request.choices:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid request payload",
                "message": "'user_selected' 값은 choices 내에 있어야 합니다.",
            },
        )

    if request.user_selected == request.correct_answer:
        return StoryCheckResponse(
            correct_answer=request.correct_answer,
            user_selected=request.user_selected,
            explanation="정답을 맞추었습니다! 잘했어요.",
        )

    try:
        response = get_story_check_response(request)
        return response

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Internal server error",
                "message": "설명을 처리하는 중 문제가 발생했습니다. 잠시 후 다시 시도해주세요.",
            },
        )
