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
source .venv/bin/activate
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
## Использование

Сервис предоставляет интерактивную документацию Swagger для тестирования эндпоинтов. По умолчанию она доступна по адресу: `http://localhost:8000/docs`

### Как пройти авторизацию:

Для выполнения защищенных запросов необходимо получить JWT-токен:

1.  **Откройте Swagger UI** (`/docs`).
2.  Нажмите кнопку **Authorize** в верхнем правом углу.
3.  В появившемся окне введите ваши учетные данные (Username и Password) в секции `OAuth2 (password flow)`.
4.  Нажмите **Authorize**, а затем **Close**. Теперь все последующие запросы будут автоматически отправлять ваш токен в заголовке `Authorization`.

---

### 📝 Основные эндпоинты

#### 1. Авторизация
*   **POST** `/api/auth/login` — Обмен логина/пароля на Access Token.

#### 2. Работа с вызовами (Calls)
*   **POST** `/api/calls` — Регистрация нового события от АТС.
    *   **Payload:**
        ```json
        {
          "call_id": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
          "phone_number": "+79876543210",
          "call_type": "incoming",
          "duration": 600
        }
        ```
    *   **Response (201):** Возвращает объект вызова с системным `id` и временем создания `created_at`.

#### 3. Проверка статуса
*   **GET** `/` — Root-эндпоинт для быстрой проверки работоспособности сервис.

---

## 🛠 Валидация и ошибки
Сервис использует **Pydantic v2** для строгой проверки входящих данных. 
*   Если данные не соответствуют схеме, API вернет **422 Validation Error** с подробным описанием того, какое поле (например, `phone_number`) заполнено некорректно.
