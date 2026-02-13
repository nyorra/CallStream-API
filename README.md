# CallStream API 📞

Асинхронный сервис на **FastAPI** для приема, валидации и сохранения данных от ATC-сервисов.

## Стек технологий

*   **Backend:** FastAPI + Uvicorn
*   **Database:** PostgreSQL + SQLAlchemy 2.0
*   **Migrations:** Alembic
*   **Validation:** Pydantic v2 & Pydantic-Settings
*   **Security:** JWT, RSA/ECDSA cryptography
*   **Infrastructure:** Docker & Docker Compose
*   **Package Manager:** uv

## Функционал

1.  **Ingestion:** Прием JSON-данных от ATC-сервисов через вебхуки.
2.  **Validation:** Строгая валидация входящих данных с помощью Pydantic-схем.
3.  **Security:** Проверка JWT-токенов (поддержка RSA/ECDSA) для авторизации запросов от сервисов.
4.  **Persistence:** Асинхронная запись данных в БД с использованием `asyncpg`.
5.  **Lifespan:** Управление жизненным циклом приложения.

## Установка и запуск

### 1. Подготовка окружения
Создайте файл `.env` в корне проекта (используйте `.env.example` как шаблон):
```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=callstream_db
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-very-secret-key
```

### 2. Запуск через Docker
```bash
docker-compose up -d --build
```
### 3. Локальный запуск (для разработки)
Используйте uv для мгновенной настройки:
```bash
uv sync
source .venv/bin/activate  # или .\.venv\Scripts\activate для Windows
uvicorn app.main:app --reload
```
### 4. Миграции базы данных (Alembic)
При внесении изменений в модели SQLAlchemy:
```bash

# Создать миграцию
alembic revision --autogenerate -m "description"

# Применить миграции
alembic upgrade head
```
## Безопасность
Сервис ожидает заголовок Authorization: Bearer <JWT_TOKEN>.
Для валидации используются библиотеки python-jose и cryptography. Настройка ключей производится через переменные окружения.
