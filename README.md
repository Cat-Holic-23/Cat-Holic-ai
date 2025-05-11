# Cat-Holic-ai

## 폴더구조

```
.
├── config/                     # 환경 설정 파일 (개발/운영)
│   ├── dev.env
│   ├── dev.env.example
│   ├── prod.env.example
│   └── staging.env.example
├── local_models/               # 로컬에서 사용하는 모델 파일 저장 디렉토리
├── moodi/                      # 주요 앱 디렉토리
│   ├── api/                    # API 엔드포인트 정의 (라우터 사용)
│   │   ├── story_gen.py        # 스토리 생성 API
│   │   ├── story_check.py      # 스토리 정답 체크 API(예정)
│   │   └── summation.py        # 학습 요약 API(예정)
│   ├── models/                 # Pydantic 스키마 및 데이터 모델
│   │   └── schemas.py
│   ├── prompts/                # 프롬프팅 관련 로직
│   │   └── story_gen.py
│   ├── utils/                  # 공통 유틸리티 함수 및 설정
│   │   ├── config.py
│   │   └── utils.py
│   └── main.py                 # FastAPI 앱 엔트리포인트
├── tests/                      # 테스트 코드
│   ├── test_story_gen.py
│   ├── test_story_check.py
│   └── test_summation.py
├── Dockerfile                  # 컨테이너화 설정(예정)
├── Makefile                    # 프로젝트 자동화 명령어 관리
├── pyproject.toml              # 프로젝트 설정 및 의존성 관리 (Poetry)
├── poetry.lock                 # 의존성 정확한 버전 관리 (Poetry)
└── README.md                   # 프로젝트 문서화

```


## 초기설치

```
poetry install
```

## API Test

```
poetry run pytest tests/test_story_gen.py -s
```