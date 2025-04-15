# Azure

## Azure의 리소스 관리 체계

1. Management Group (관리 그룹)

큰 조직 내에서 리소스를 효율적으로 운영하고자 할 때 사용

관리 그룹 내 관리 그룹 존재 가능

**사용 목적**

-   계층적 관리
-   여러 구독에 대한 액세스 권한 관리

2. Subscription (구독)

리소스를 관리하고, `비용을 지불하는 기본 단위`

하나의 리소스는 하나의 구독과 연결

**사용 목적**

-   엑세스 권한 제어
-   실행 환경 분리
    -   ex) 테스트 환경, 프로덕션 환경 구분을 구독 단위로 네트워크 망. 즉, 실행환경 분리

3. Resource Groups (리소스 그룹)

리소스 들을 묶어서 관리하는 단위,

모든 리소스는 특정 리소스 그룹에 속해야 함

**사용 목적**

-   배포 자동화
-   라이프 사이클 관리
-   그룹 단위 리소스 복제

```
└─ Management Group (관리 그룹)
        │
        ├─ Subscription (구독)
        │
        ├─ Subscription (구독)
        │       │
        │       └─ Resource Groups (리소스 그룹)
        │                │
        │                ├─ Blob Storage
        │                │
        │                ├─ Azure Function
        │                │
        │                ├─ Service Bus
        │                │
        ...              ...
```

## Azure Blob Storage
