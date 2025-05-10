import logging
import os

from dotenv import load_dotenv


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s - %(message)s",
    )


def load_config(env_path: str = "../config/dev.env") -> None:
    load_dotenv(env_path)


def get_gemini_api_key() -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY 환경변수가 설정되지 않았습니다.")
    return api_key
