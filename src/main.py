from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage
from utils import load_config, get_gemini_api_key

def main():
    # 환경변수 로딩
    load_config()

    # Gemini API Key 설정
    api_key = get_gemini_api_key()

    # LangChain과 Gemini 모델 연결
    chat_model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=api_key
    )

    # 시스템 메시지로 역할 정의
    system_message = SystemMessage(content="당신은 사용자의 질문에 친절히 답하는 AI 어시스턴트입니다.")

    # 사용자 입력 받아 응답 출력 (무한루프)
    print("Gemini와 대화를 시작합니다. 종료하려면 '종료'를 입력하세요.")
    while True:
        user_input = input("사용자: ")
        if user_input.strip().lower() == "종료":
            print("대화를 종료합니다.")
            break

        # LangChain 메시지 형식으로 전송
        messages = [
            system_message,
            HumanMessage(content=user_input)
        ]

        print(messages)

        # # 응답 받기
        # response = chat_model(messages)

        # # 응답 출력
        # print(f"Gemini: {response.content}")

if __name__ == "__main__":
    main()
