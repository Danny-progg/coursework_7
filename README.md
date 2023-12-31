# AtomicHabits: Трекер полезных привычек
## Исползуемые технологии
  * python
  * django
  * django rest framework
  * drf-yasg
  * postgresql
  * redis
  * celery
  * django-celery-beat
  * cors
  * simple jwt

## Сущности системы
  ### Привычка
  * пользователь
  * место выполнения
  * время выполнения
  * действие
  * связанная привычка (опционально)
  * признак приятной привычки
  * периодичность
  * вознаграждение
  * время на выполнение
  * признак публичности

### Пользователь
* почта
* пароль
* телефон 
* город 
* аватар
* telegram id 


## Документация API
Документация для API реализована с помощью drf-yasg и находится на следующих эндпоинтах:
* http://127.0.0.1:8000/docs/
* http://127.0.0.1:8000/redoc/

## CORS
Для безопасности API реализован CORS с помощью django-cors-headers. 

В модуле ``settings.py`` необходимо внести изменения в следующие настройки, если у Вас есть сторонние домены, обращающиеся к Вашему API:

```
CORS_ALLOWED_ORIGINS = [
    "https://read-only.example.com",
    "https://read-and-write.example.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com",
]
```

## Как использовать данный проект?

- Клонировать репозиторий и перейти в директорию
  
  В терминале необходимо ввести команды:
  ```
  git clone https://github.com/Danny-progg/coursework_7
  ```
  ```
  cd AtomicHabits/
  ```
 
- Создать файл ``.env``, который необходимо заполнить данными из файла ``env.sample``
- Далее необходимо выполнить следующие команды в терминале (важно иметь открытым программу Docker Dekstop):
  ```
  docker-compose build
  ```
  ```
  docker-compose up
  ```
- Откройте браузер и перейдите по адресу http://127.0.0.1:8000 для доступа к приложению.
