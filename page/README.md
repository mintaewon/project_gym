# Install


- OS에 맞는 nodejs 설치
- Docker, Docker compose 설치

```
docker pull mysql:8.0-debian
```

- 사용하기 위해서는 DB를 생성해야함

- MySQL 접속 후

```sql
CREATE DATABASE gym;
USE gym;
```

- page 폴더 최상단에 `.env` 파일 생성

```
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_HOST=
MYSQL_PORT=
MYSQL_DATABASE=gym

SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```


- 터미널에서
```bash
source install.sh
```
<!-- -- docker-compose down

-- docker-compose up -d --build -->