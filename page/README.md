# Install


- OS에 맞는 nodejs 설치
- Docker, Docker compose 설치

# Use
```
docker-compose up -d --build
```

- 단, local 사용은 데이터베이스와 테이블 생성을 해야함.

- MySQL 접속 후

```sql
CREATE DATABASE GYM;
USE GYM;

CREATE TABLE TIMELINE
(
    DateTime varchar(30),
    Weather varchar(10),
    UseMachines varchar(50),
    PRIMARY KEY(DateTime)
);
```

- 컨테이너 종료 후 다시 실행

```
docker-compose down

docker-compose up -d --build
```