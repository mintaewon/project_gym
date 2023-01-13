# Install


- OS에 맞는 nodejs 설치
- Docker, Docker compose 설치

# Use
```
docker pull mysql:8.0-debian

docker-compose up -d --build
```

- 사용하기 위해서는 테이블 생성해야함
- MySQL 접속 후

```sql
CREATE TABLE TIMELINE
(
    DateTime varchar(30),
    Weather varchar(10),
    UseMachines varchar(50),
    PRIMARY KEY(DateTime)
);
```
- app/config.json 에 DB접속 정보 입력
- 컨테이너 종료 후 다시 실행

```
docker-compose down

docker-compose up -d --build
```