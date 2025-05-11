import os

from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI


def get_chat_model():
    api_key = os.getenv("GEMINI_API_KEY")
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash", google_api_key=api_key
    )


response_schemas = [
    ResponseSchema(name="story", description="스토리"),
    ResponseSchema(name="question", description="질문"),
    ResponseSchema(name="choices", description="선택지"),
    ResponseSchema(name="correct_answer", description="정답"),
]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
