# Платформа ценообразования Авито (бэкенд)
## _Решение трека Avito от команды BruhMisis для хакатона Purple It Hack_

Бэкенд-приложение выполнено на фрейморке Python FastAPI. 

## Фичи
- авторизация через JWT 
- система контроля изменений для сохранения изменений цен 
- сервис отправки цен пользователям
- хранение данных в PostgreSQL 
- кеширование в Redis
- ✨ документация в Swagger UI ✨

## Требования перед установкой
### Docker engine
Установка на Linux: https://docs.docker.com/engine/install/ubuntu/ <br>
Установка на Windows: https://docs.docker.com/desktop/install/windows-install/ <br>
Установка на Mac: https://docs.docker.com/desktop/install/mac-install/ <br>

## Установка
    git clone https://github.com/Auxxxxx/purple-avito-backend-bruh_misis
    cd purple-avito-backend-bruh_misis/
    cp .env.example .env
    docker compose up -d

| Библиотека       | Документация                                               |
|------------------|------------------------------------------------------------|
| FastAPI          | https://github.com/tiangolo/fastapi/blob/master/README.md] |
| SQLAlchemy       | https://docs.sqlalchemy.org/en/20/                         |
| Psychopg         | https://www.psycopg.org/docs/                              |

GitHub репозиторий фронтенд-приложения