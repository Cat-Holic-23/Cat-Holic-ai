.PHONY: all format lint test check

# isort와 black 코드 스타일 정리
format:
	poetry run isort .
	poetry run black .

# flake8 코드 스타일 위반 사항 검사
lint:
	poetry run flake8 .

# pytest 테스트 실행
test:
	poetry run pytest

# 포맷팅, 린팅, 테스트 순차적 실행
check: format lint test

# 기본 명령어: check를 기본 설정
all: check
