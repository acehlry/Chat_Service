# Azure Service Bus

- Azure의 메시징 서비스
    - 비동기 통신
    - 결합도 하락
        - API, AGENT가 분리되어 각 기능이 추가될떄 각각 소스만 수정
    - 부하 분산
        - 인스턴스가 늘어남에 따라서 부하가 줄어든다
    - 스케일링 / 유연성


## Service Bus의 특징

1. 큐
    - FIFO 방식으로 메시지 처리
    - 메시지를 수신하면 처리하고 제거
        - 1:1 방식
        - 처리에 실패한 경우 DLQ(Dead Lector Queue)를 사용할 수 있음
2. 토픽/구독
    - 여러 구독(Subscriber)이 동일한 메시지를 받아서 독립적으로 처리할 수 있음
    - 각 구독은 메시지 필터를 설정할 수 있음


## Azure Function과의 결합

- 큐의 메시지를 감지하여 Function의 실행이 가능
    - 메시지를 받아오는 코드를 짤 필요없음
- Cosmos DB, Blob Storage 등 다른 소스들도 가능

