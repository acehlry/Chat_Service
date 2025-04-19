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

- `비동기` 지원
- 타입 힌트를 통한 자동 `데이터 검증`
- 쉬운 확장성
- API 문서 자동 생성

## 실행

```sh
# main: 파일 이름
# app: 인스턴스 이름
# -reload: 변경 확인시 서버 재기동
uvicorn main:app --reload
```

## 서버리스

- 개발자가 서버 세팅에 신경 X
    - 비지니스 로직 구현만 집중
- 함수 실행, 리소스 사용 등 사용량 만큼 비용을 지불
- 이벤트 기반 Function 실행
    - HTTP 요청, MQ 탐지, 파일 업로드, DB 업데이트 등등

**장점**

1. 비용 절감
2. Auto-Scaling 편리
    - 인스턴스의 성능이 느리다고 판단하면, 알아서 늘린다
3. 개발 속도 및 생산성 향상
    - 서버 설정할 필요가 없기 때문

**단점**

1. 콜드 스타트(첫 요청 지연)
    - 인스턴스가 안 떠있는 상태, 생서하는데 시간이 걸림
    - Pre-warmed Instance를 이용해서 해결 할 수 있음(요금 지불)
    - 언어별로 시간이 다름(Java의 경우...)
2. Stateless 모델
    - 상태 유지가 힘듬
    - 함수가 호출이 될때, 이전의 상태를 가지고 있지 않음(로그인이 되어있었는지...)
        - DB, Redis등을 이용해서 상태를 기억해야함
3. 서버에 대한 자유도 부족
4. 플랫폿에 대한 종속성 발생
    - 해당 플랫폼에 코드를 맞춰 작성해야하기 때문

## Auzre Function으로 변경

```sh
npm install -g azure-function-core-tools
```