from fastapi.testclient import TestClient
from moodi.main import app
from moodi.utils.config import load_config

load_config(env_path="config/dev.env")

client = TestClient(app)

def test_story_check_wrong_answer():
    response = client.post(
        "/gemini/story-check",
        json={
            "story": "민수는 새 학년이 시작되어 자기소개를 하기로 했어요. 민수는 자기소개를 하려고 교실 앞에 섰는데 갑자기 마음이 불안해졌어요. 친구들이 자기를 보고 있었기 때문이에요. 민수의 표정이 어두워지고 눈가가 촉촉해졌어요.",
            "question": "민수는 지금 어떤 감정을 느끼고 있을까요?",
            "choices": ["기쁨", "슬픔", "화남", "편안함"],
            "correct_answer": "슬픔",
            "user_selected": "화남",
        },
    )

    assert response.status_code == 200
    result = response.json()
    print(result)

    assert result["correct_answer"] == "슬픔"
    assert result["user_selected"] == "화남"
    assert "슬픔" in result["explanation"]

def test_story_check_correct_answer():
    response = client.post(
        "/gemini/story-check",
        json={
            "story": "민수는 자기소개를 하려고 교실 앞에 섰는데 마음이 불안해졌어요. 친구들이 자기를 보고 있었기 때문이에요. 민수의 표정이 어두워지고 눈가가 촉촉해졌어요.",
            "question": "민수는 지금 어떤 감정을 느끼고 있을까요?",
            "choices": ["기쁨", "슬픔", "화남", "편안함"],
            "correct_answer": "슬픔",
            "user_selected": "슬픔",
        },
    )

    assert response.status_code == 200
    result = response.json()
    print(result)

    assert result["correct_answer"] == "슬픔"
    assert result["user_selected"] == "슬픔"
    assert "정답을 맞추었습니다" in result["explanation"]
