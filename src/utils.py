import logging
import os

from dotenv import load_dotenv


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s - %(message)s",
    )


def load_config(env="dev"):
    load_dotenv(f"config/{env}.env")
    return {
        "API_KEY": os.getenv("API_KEY"),
    }
