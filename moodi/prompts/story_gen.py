from moodi.utils.utils import get_chat_model, output_parser
from moodi.models.schemas import StoryRequest, StoryResponse
from langchain.prompts import PromptTemplate

story_prompt = PromptTemplate(
    template="나이: {age}살\n상황: {social_situation}\n히스토리: {learning_history_summary}\n\n스토리, 질문, 선택지 4개, 정답을 생성해주세요.\n{format_instructions}",
    input_variables=["age", "social_situation", "learning_history_summary"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()}
)

def get_story_response(request: StoryRequest) -> StoryResponse:
    chat_model = get_chat_model()

    formatted_prompt = story_prompt.format(
        age=request.age,
        social_situation=request.social_situation,
        learning_history_summary=request.learning_history_summary
    )

    response = chat_model.invoke(formatted_prompt)
    parsed_response = output_parser.parse(response.content)

    return StoryResponse(**parsed_response)
