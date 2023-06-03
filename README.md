## Проект YaMDb

#### Описание проекта:
Проект YaMDb собирает отзывы пользователей на произведения, такие как книги, фильмы и музыка. Категории произведений включают «Книги», «Фильмы» и «Музыку», но список можно расширить, добавив новые категории, например, «Изобразительное искусство» или «Ювелирку».

Каждому произведению можно присвоить жанр из предустановленного списка, таких как «Сказка», «Рок» или «Артхаус».

Только администраторы имеют права добавлять произведения, категории и жанры.

Пользователи могут оставлять текстовые отзывы и ставить оценку произведению в диапазоне от одного до десяти (целое число). Из пользовательских оценок формируется усредненная оценка произведения - рейтинг (целое число). Каждый пользователь может оставить только один отзыв к произведению.

Пользователи могут оставлять комментарии к отзывам.

Для добавления отзывов, комментариев и ставления оценок пользователь должен быть аутентифицирован.

#### Технологии:
[![Python Icon](https://camo.githubusercontent.com/a00abd8cea4105fa1cad91f7235d11206b492f51afeb9b23a25d04e8f36935e3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d4646443433423f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d626c7565)](https://www.python.org/)[![Django](https://camo.githubusercontent.com/dd7f390cf162d4b963b26215e6cd4373282ebe20caccfd4ef479798c2b590e38/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d677265656e)](https://www.djangoproject.com)[![Django REST](https://camo.githubusercontent.com/4a6c6851aab9b0042c0baaea2c61993ea052cff554d8a3d42cd51d67d304d452/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646a616e676f253230726573742d6666313730393f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465)](https://www.django-rest-framework.org/)[![JWT](https://camo.githubusercontent.com/92407fc26e09271d8137b8aaf1585b266f04046b96f1564dfe5a69f146e21301/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a57542d3030303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d4a534f4e253230776562253230746f6b656e73266c6f676f436f6c6f723d7768697465)](https://github.com/jazzband/djangorestframework-simplejwt)

#### Используемые пакеты:
```
requests==2.26.0
Django==3.2
djangorestframework==3.12.4
PyJWT==2.1.0
pytest==6.2.4
pytest-django==4.4.0
pytest-pythonpath==0.7.3
djangorestframework-simplejwt==4.7.2
django-filter==23.2
python-dotenv==0.21.1

```



#### Установка
##### 1. Клонировать репозиторий:
```
git clone ...
```
##### 2. Перейти в папку с проектом:
```
cd api_yamdb/
```
##### 3. Установить виртуальное окружение для проекта:
```
python -m venv venv
```
##### 4. Активировать виртуальное окружение для проекта:
```
# для OS Lunix и MacOS
source venv/bin/activate
# для OS Windows
source venv/Scripts/activate
```
##### 5. Установить зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
##### 6. Выполнить миграции на уровне проекта:
```
cd api_yamdb
python manage.py migrate
```
##### 7. Запустить проект:
```
python manage.py runserver
```


#### Дополнительно
- Для загрузки данных в составе проекта используйте  management-команды, которые добавляют данные в базу данных через Django ORM.

- После выполения миграций загрузить данные CSV из папки static проекта, можно с помощью следующих команд:
```
python manage.py load_csv_user
python manage.py load_csv_category
python manage.py load_csv_genre
python manage.py load_csv_title
python manage.py load_csv_review
python manage.py load_csv_comment
python manage.py load_csv_genre_title

```
#### После запуска проекта документация API будет доступна по адресу:
```
http://127.0.0.1:8000/redoc/
```

#### Примеры запросов
- Пример POST-запроса:
    Регистрация нового пользователя и получение confirmation_code. Доступно без 
    токена.
    POST http://127.0.0.1:8000/api/v1/auth/signup/
```
{
    "email": "user@example.com",
    "username": "string"
}
```
- Пример ответа:
````
{
    "email": "string",
    "username": "string"
}
````
В проекте настроен filebased способ отправки почты, confirmation_code будет находится в папке send_email базовой директории.

- Получение JWT-токена в обмен на username и confirmation_code. Доступно без токена.
POST http://127.0.0.1:8000/api/v1/auth/token/
```
{
    "username": "string",
    "confirmation_code": "string"
}
```
- Пример ответа:
````
{
    "token": "string"
}
````
В дальнейшем token передаётся в Header: Bearer
- Создание отзыва к произведению. Необходим токен.
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
````
{
    "text": "string",
    "score": 1
}
````
- Пример ответа:
````
{
    "id": 0,
    "text": "string",
    "author": "string",
    "score": 1,
    "pub_date": "2019-08-24T14:15:22Z"
}
`````

#### Авторы проекта
* [Sergey Samorukov](https://github.com/bauman1922)
* [Veronika Lapteva](https://github.com/VeronikaLapteva)
* [Daniil Malyshev](https://github.com/YaStirayuLaskoy)
