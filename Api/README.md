# FastApi

-   파이썬 기반 웹 프레임워크

    -   API 만드는데 주로 사용

-   Python .8+
-   자체 ORM 제공 X
    -   SQLAlchemy

## FastAPI 성능

- Starlette
    - 경량 ASGI 프레임워크
        - Asynchronous
        - Server
        - Gateway
        - Interface

- Pydantic
    - 데이터 검증
        - 데이터 검증
        - 자동 형변환
    - 직렬화
        - json으로 직렬화하기 편함 --> API 문서 자동으로 생성        

## 코드

```py
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
        return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

- `Union`: 리스트 안에 있는 어떤 타입도 받을 수 있음

## FastAPI 특징

- 비동기 지원
- 타입 힌트를 통한 자동 데이터 검증
- 쉬운 확장성
- API 문서 자동 생성

## 실행

```sh
# main: 파일 이름
# app: 인스턴스 이름
# -reload: 변경 확인시 서버 재기동
uvicorn main:app --reload
```