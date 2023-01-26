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

터미널에서
```bash
source install.sh
```
<!-- -- docker-compose down

-- docker-compose up -d --build -->