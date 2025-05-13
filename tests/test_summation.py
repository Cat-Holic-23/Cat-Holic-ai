from fastapi.testclient import TestClient
from moodi.main import app
from moodi.utils.config import load_config

load_config(env_path="config/dev.env")

client = TestClient(app)

def test_summation():
    response = client.post(
        "/local/summation",
        json={
            "recent_answers": [
                {
                    "story": "민수가 친구와 싸우고 울었어요.",
                    "question": "민수의 기분은 어떤가요?",
                    "user_selected": "화남",
                    "correct_answer": "슬픔"
                },
                {
                    "story": "친구가 놀이터에서 놀다가 넘어졌어요.",
                    "question": "친구는 어떤 기분일까요?",
                    "user_selected": "기쁨",
                    "correct_answer": "아픔"
                }
            ]
        },
    )

    assert response.status_code == 200
    result = response.json()
    print(result)

    assert "learning_history_summary" in result
    assert len(result["learning_history_summary"]) > 0

def test_summation_invalid_payload():
    response = client.post(
        "/local/summation",
        json={"recent_answers": []},  # 빈 리스트 전달
    )

    assert response.status_code == 400
    result = response.json()
    print(result)

    assert result["detail"]["error"] == "Invalid request payload"
    assert result["detail"]["message"] == "'recent_answers'는 최소 1개 이상 최대 10개의 항목을 포함해야 합니다."
