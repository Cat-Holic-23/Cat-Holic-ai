from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import PromptTemplate

from moodi.models.schemas import SummationRequest, SummationResponse
from moodi.utils.utils import get_chat_model

response_schemas = [
    ResponseSchema(
        name="learning_history_summary",
        description="학습 히스토리의 요약 분석 결과",
    )
]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

summation_prompt = PromptTemplate(
    template="""다음은 최근 사용자가 문제를 풀고 선택한 답변들입니다.
사용자가 어떤 유형의 감정을 이해하는 데 어려움이 있는지 요약하여 분석해주세요.

최근 답변들:
{recent_answers}

{format_instructions}
""",
    input_variables=["recent_answers"],
    partial_variables={
        "format_instructions": output_parser.get_format_instructions()
    },
)


def get_summation_response(request: SummationRequest) -> SummationResponse:
    chat_model = get_chat_model()

    formatted_answers = "\n".join(
        [
            f"- 스토리: {ans.story}\n  질문: {ans.question}\n  사용자 선택: {ans.user_selected}, 정답: {ans.correct_answer}"
            for ans in request.recent_answers
        ]
    )

    formatted_prompt = summation_prompt.format(
        recent_answers=formatted_answers
    )
    response = chat_model.invoke(formatted_prompt)
    parsed_response = output_parser.parse(response.content)

    return SummationResponse(
        learning_history_summary=parsed_response["learning_history_summary"]
    )
