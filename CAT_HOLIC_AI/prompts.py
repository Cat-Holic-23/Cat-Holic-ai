from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

response_schemas = [
    ResponseSchema(name="story", description="생성된 스토리"),
    ResponseSchema(name="question", description="질문"),
    ResponseSchema(name="choices", description="4개의 선택지"),
    ResponseSchema(name="correct_answer", description="정답"),
]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

story_prompt = PromptTemplate(
    template=(
        "나이는 {age}살이고, 상황은 '{social_situation}'입니다. "
        "학습 히스토리는 '{learning_history_summary}'입니다. "
        "이를 바탕으로 간단한 스토리와 질문, 4개의 선택지, 정답을 만들어 주세요.\n"
        "{format_instructions}"
    ),
    input_variables=["age", "social_situation", "learning_history_summary"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()}
)
