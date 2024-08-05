# ParitetTest
Веб приложение с возможностью создавать, удалять и просматривать Изображения с описанием.
Реализованно на DRF + Vue JS
---
# DRF
У API есть 3 эндпоинта
1. Создание изображения с описанием
   - Эндпоинт: `POST /api/api-auth/images/`
   - Принимает JSON с изображением в формате base64 и текстовым описанием
   - Пример запроса: <br/>  `{
    "image": "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2w...",
    "description": "Описание изображения"
}`
2. Получение списка всех изображений с описаниями
   - Эндпоинт: `GET /api/api-auth/images/`
   - Отдает список обьектов с URL изображения и его описанием
   - Пример ответа: <br/>  `{
   "id": 1,
   "image_url": "http://example.com/media/images/image1.png",
   "description": "Описание изображения 1"
}`
3. Удаление изображения по ID
    - Эндпоинт: `DELETE /api/api-auth/images/{id}/`
    - Удаляет изображение с указаным ID
---
# Установка и запись
### Колнирование репозитория
 - `git clone https://github.com/Qwiple123/ParitetTest.git`
 - `cd ParitetTest`
### Создание и настройка .env файла
 - `cp backend/.env.template backend/.env`
 - Затем при необходимости отредактируйте .env файл (По умолчанию .env уже заполнен для удобства)
### Установка Docker
- Убедитесь что Docker и DockerCompose установлен
### Запуск проекта
- Перейдите в корневую директорию и запустите контейнеры Docker
- `docker-compose up --build`
---
# Использование
## Доступ к приложению 
 - Django API будет доступно по адресу: http://localhost/api/api-auth/
 - Vue.js frontend будет доступен по адресу: http://localhost/
