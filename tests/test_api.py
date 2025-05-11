from fastapi.testclient import TestClient
from CAT_HOLIC_AI.main import app  # main.py의 FastAPI 인스턴스를 import
from CAT_HOLIC_AI.utils import load_config 


# 테스트 실행 전 환경변수 로딩
load_config(env_path="config/dev.env")

client = TestClient(app)

def test_generate_story():
    response = client.post(
        "/generate-story",
        json={
            "age": 10,
            "social_situation": "새로운 학년이 시작되어 자기소개를 해야 하는 상황",
            "learning_history_summary": "지난 학습동안 슬픈 감정을 이해하기 어려워하는 경향이 있음",
        },
    )

    assert response.status_code == 200
    result = response.json()
    print(result)  # 결과 확인을 위해 출력

    assert "story" in result
    assert "question" in result
    assert len(result["choices"]) == 4
    assert result["correct_answer"] in result["choices"]
