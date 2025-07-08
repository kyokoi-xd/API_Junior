# Auth Service

Минимальный сервис аутентификации на FastAPI с PostgreSQL и Docker.

## Требования

- Docker
- Docker Compose

## Быстрый старт

Скопируйте файл с переменными окружения:

   ```bash
   cp .env .env

docker-compose up -d

curl http://localhost:8000/
# Ответ: {"message": "Service is up and running"}

Откройте Swagger UI для документации API:

http://localhost:8000/docs