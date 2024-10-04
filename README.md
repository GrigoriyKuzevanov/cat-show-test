# Cat Show
API приложение, построенное с использованием фреймворка FastAPI. Выполнено в качестве тестового задания.

## Основные инструменты
 - Python
 - [FastApi](https://fastapi.tiangolo.com/) фреймворк для разработки веб-приложений на языке python
 - [PostgreSQL](https://www.postgresql.org/) система управления реляционными базами данных
 - [SQLAlchemy](https://www.sqlalchemy.org/) мощный инструмент для работы с реляционными базами данных на языке python
 - [Alembic](https://alembic.sqlalchemy.org/en/latest/) инструмент миграция для sqlalchemy
 - [Pytest](https://docs.pytest.org/en/stable/) фреймворк для написания тестов

## Установка
Клонировать гит репозиторий на свою машину и перейти в директорию проекта:
```sh
git clone https://github.com/GrigoriyKuzevanov/cat-show-test.git
cd cat-show-test/
```
**В директории проекта создать файл .env, в котором необходимо указать несколько переменных. Для быстрого старта приложения можете использовать значения переменных из примера или заменить значения своими:**

```
# настройки основной базы данных
DB_USER=cat-show-db-user
DB_PASSWORD=cat-show-db-password
DB_HOST=db-main # не изменять, если приложение запускается с помощью docker
DB_PORT=5432 # не изменять, если приложение запускается с помощью docker
DB_NAME=cat-show-db
ECHO_SQL=False  # вы можете изменить, если хотите видеть SQL запросы формируемые приложением

# настройки тестовой базы данных
TEST_DB_USER=cat-show-db-user-test
TEST_DB_PASSWORD=cat-show-db-password-test
TEST_DB_HOST=db-test  # не изменять, если приложение запускается с помощью docker
TEST_DB_PORT=5432  # не изменять, если приложение запускается с помощью docker
TEST_DB_NAME=cat-show-db-test

# настройка CORS
# write down your origins or set it to '*' for all origins
# EXAMPLE: CORS_ORIGINS=www.example.com, www.hello.com, www.github.com
CORS_ORIGINS=*
```

# Использование
**Запустить контейнеры с приложением и базами данных:**
```sh
docker compose up
```

**После запуска в docker compose, сервис Pytest выполняет тестирование API. Результат можно увидеть в консоли при запуске не в detached mode:**
```sh
pytest-1   | ============================= test session starts ==============================
pytest-1   | platform linux -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0 -- /usr/local/bin/python3.12
pytest-1   | cachedir: .pytest_cache
pytest-1   | rootdir: /usr/src/cat-show-test
pytest-1   | plugins: anyio-4.6.0
pytest-1   | collecting ... collected 22 items
pytest-1   | 
pytest-1   | tests/test_api/test_breeds.py::test_get_breeds PASSED                    [  4%]
pytest-1   | tests/test_api/test_kittens.py::test_get_kittens PASSED                  [  9%]
pytest-1   | tests/test_api/test_kittens.py::test_get_kittens_by_breed PASSED         [ 13%]
pytest-1   | tests/test_api/test_kittens.py::test_get_kitten[1] PASSED                [ 18%]
pytest-1   | tests/test_api/test_kittens.py::test_get_kitten[2] PASSED                [ 22%]
pytest-1   | tests/test_api/test_kittens.py::test_get_kitten[3] PASSED                [ 27%]
pytest-1   | tests/test_api/test_kittens.py::test_get_kitten_not_exists[1] PASSED     [ 31%]
pytest-1   | tests/test_api/test_kittens.py::test_get_kitten_not_exists[2] PASSED     [ 36%]
pytest-1   | tests/test_api/test_kittens.py::test_get_kitten_not_exists[3] PASSED     [ 40%]
pytest-1   | tests/test_api/test_kittens.py::test_post_kitten PASSED                  [ 45%]
pytest-1   | tests/test_api/test_kittens.py::test_post_kitten_with_breed_not_exist PASSED [ 50%]
pytest-1   | tests/test_api/test_kittens.py::test_update_kitten PASSED                [ 54%]
pytest-1   | tests/test_api/test_kittens.py::test_update_kitten_not_exist[1] PASSED   [ 59%]
pytest-1   | tests/test_api/test_kittens.py::test_update_kitten_not_exist[2] PASSED   [ 63%]
pytest-1   | tests/test_api/test_kittens.py::test_update_kitten_not_exist[3] PASSED   [ 68%]
pytest-1   | tests/test_api/test_kittens.py::test_update_kitten_with_breed_not_exist PASSED [ 72%]
pytest-1   | tests/test_api/test_kittens.py::test_delete_kitten[1] PASSED             [ 77%]
pytest-1   | tests/test_api/test_kittens.py::test_delete_kitten[2] PASSED             [ 81%]
pytest-1   | tests/test_api/test_kittens.py::test_delete_kitten[3] PASSED             [ 86%]
pytest-1   | tests/test_api/test_kittens.py::test_delete_kitten_not_exist[1] PASSED   [ 90%]
pytest-1   | tests/test_api/test_kittens.py::test_delete_kitten_not_exist[2] PASSED   [ 95%]
pytest-1   | tests/test_api/test_kittens.py::test_delete_kitten_not_exist[3] PASSED   [100%]
pytest-1   | 
pytest-1   | ============================== 22 passed in 2.08s ==============================
pytest-1 exited with code 0
```

**Вы можете создать начальные данные для провеки.**
- Узнайте id контейнера приложения:
```sh
docker ps
```
- Войдите в контейнер приложения:
```sh
docker exec -it <container-id> bash
```
- Выполните скрипт создания начальных данных:
```sh
python3 -m src.app.scripts.create_initial_data
```

> [!WARNING]  
> Скрипт создания начальных данных должен использоваться только один раз перед работой с API

**Для доступа к API перейдите в браузере:**
```
http://<your ip address>:8080/docs
```

**Для доступа к API вы также можете использовать коллекцию Postman: файл `Cat Show.postman_collection.json` в рабочей директории проекта. Для использования, необходимо создать указать значение переменной URL (по умолчанию значение: localhost:8080)**

# Доступные методы API
- **Get Breeds** Получение списка пород
- **Get Kittens** Получение списка всех котят
- **Get Kittens By Breed** Получение списка котят определенной породы по фильтру.
- **Get Kitten** Получение подробной информации о котенке.
- **Create Kitten** Добавление информации о котенке
- **Update Kitten** Изменение информации о котенке
- **Delete Kitten** Удаление информации о котенке
