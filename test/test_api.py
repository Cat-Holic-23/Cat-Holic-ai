from fastapi.testclient import TestClient
from moodi.main import app
from moodi.utils.config import load_config  # 변경한 폴더명(utils)에 맞게 import 수정

load_config(env_path="config/dev.env")

client = TestClient(app)

def test_generate_story():
    response = client.post(
        "/gemini/story_gen", 
        json={
            "age": 10,
            "social_situation": "새로운 학년이 시작되어 자기소개를 해야 하는 상황",
            "learning_history_summary": "지난 학습동안 슬픈 감정을 이해하기 어려워하는 경향이 있음",
        },
    )

    assert response.status_code == 200
    result = response.json()
    print(result)

    assert "story" in result
    assert "question" in result
    assert len(result["choices"]) == 4
    assert result["correct_answer"] in result["choices"]
