from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import PromptTemplate

from moodi.models.schemas import StoryCheckRequest, StoryCheckResponse
from moodi.utils.utils import get_chat_model

response_schemas = [
    ResponseSchema(name="explanation", description="정답에 대한 자세한 해설")
]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

story_check_prompt = PromptTemplate(
    template="""다음 스토리와 질문, 사용자의 선택을 보고 정답과 사용자가 고른 답이 왜 다른지 친절하게 설명해주세요.

스토리: {story}
질문: {question}
선택지: {choices}
정답: {correct_answer}
사용자 선택: {user_selected}

{format_instructions}
""",
    input_variables=[
        "story",
        "question",
        "choices",
        "correct_answer",
        "user_selected",
    ],
    partial_variables={
        "format_instructions": output_parser.get_format_instructions()
    },
)


def get_story_check_response(request: StoryCheckRequest) -> StoryCheckResponse:
    chat_model = get_chat_model()

    formatted_prompt = story_check_prompt.format(
        story=request.story,
        question=request.question,
        choices=", ".join(request.choices),
        correct_answer=request.correct_answer,
        user_selected=request.user_selected,
    )

    response = chat_model.invoke(formatted_prompt)
    parsed_response = output_parser.parse(response.content)

    return StoryCheckResponse(
        correct_answer=request.correct_answer,
        user_selected=request.user_selected,
        explanation=parsed_response["explanation"],
    )
