# Azure Cosmos DB

글로벌 분산 멀티모델 데이터베이스 서비스

- `글로벌 분산`: 전세계 여러 지역에 복제
    - 어디서 접근을 하더라도 낮은 지연

- `멀티모델`
    - 문서, Key-Value, 그래프 등 다양한 데이터 모델을 지원
    - SQL, MongoDB, Cassandra, Gremlin 등 다양한 API, 언어를 통한 접근 가능


## 보안

- 데이터 암호화
    - 저장 및 전송(SSL/TLS) 중 모두 암호화 제공
- Azure Active Directory와 통합
    - ID 및 액세스 관리 서비스
        - 다단계 인증, 조건부 액세스 정책, 접근 권한 관리 등등
        - ex) 특정 위치에서만 접근, 데이터 별 권한 분리

## 동작 및 생성 방싱

1. `Request Unit 기반`

- RU 단위 비용 계산 및 자원 할당
    - 1 KB Read  = 1RU
    - 1 KB Write = 5RU
- 자동 또는 수동으로 RU/s를 조절하여 확장 또는 축소
- 할당한 RU만큼만 비용 지불, Autoscaling을 통한 비용 최적화

- 요약: 세분화된 리소스 관리 비용 최적화 제공

2. `vCore Cluster 기반`

- vCore 기반 처리량, 저장공간 관리
    - 서버 요금제, 월별로 고정 요금
- 클러스터의 크기를 조절하며 처리량과 저장공간을 확장
- 서버 요금제 만큼 비용 지불

- 요약: 대규모 애플리케이션 및 대용량 데이터 처리에 최적화

## Request Unit 방식

1. `Provisioned Throughput`

- 테이블 별 RU 할당, 할당 RU만큼 비용 지불

2. `Serverless`

- 사용한 RU만큼 비용 지불