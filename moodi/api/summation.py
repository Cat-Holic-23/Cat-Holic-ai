from fastapi import APIRouter, HTTPException

from moodi.models.schemas import (
    ErrorResponse,
    SummationRequest,
    SummationResponse,
)
from moodi.prompts.summation import get_summation_response

router = APIRouter()


@router.post(
    "/summation",
    response_model=SummationResponse,
    responses={
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
        503: {"model": ErrorResponse},
    },
)
async def summation(request: SummationRequest):
    if not (1 <= len(request.recent_answers) <= 10):
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid request payload",
                "message": "'recent_answers'는 최소 1개 이상 최대 10개의 항목을 포함해야 합니다.",
            },
        )

    try:
        response = get_summation_response(request)
        return response

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Internal server error",
                "message": "학습 이력을 분석하는 중에 문제가 발생했습니다. 다시 시도해주세요.",
            },
        )
