# Менеджер задач

## Описание
**Менеджер задач** – это веб-приложение, разработанное при помощи фреймворка Django. В данном приложении можно создавать проекты, добавлять задания и участников, брать на исполнение задачи и изменять их статус.

## Стек технологий

**Django 5.0.3** <br>
**PostgreSQL** <br>
**AJAX(JQuery 3.5.1)**<br>

<details>
<summary><b> 
  
  ## Структура проекта</b>
  
</summary>
  
  ```bash 
TASK_MANAGEMENT
│   data_dump.json
│   manage.py
│   README.md
│   requirements.txt
│
├───accountApp
│   │   admin.py
│   │   apps.py
│   │   forms.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           __init__.cpython-311.pyc
│   │
│   ├───static
│   │   └───accountApp
│   │       └───CSS
│   │               login.css
│   │
│   └───templates
│       └───accountApp
│           └───Html
│                   login.html
│                   register.html
│
├───mainApp
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │       __init__.py
│   │
│   ├───static
│   │   └───mainApp
│   │       ├───CSS
│   │       │       base.css
│   │       │       error.css
│   │       │       index.css
│   │       │
│   │       └───img
│   │               logo.png
│   │
│   └───templates
│       └───mainApp
│           └───Html
│                   base.html
│                   error.html
│                   index.html
│
├───projectsApp
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │       0001_initial.py
│   │       0002_remove_projectmodel_author_and_more.py
│   │       0003_taskmodel_is_ready_alter_taskmodel_user.py
│   │       0004_temporary_links.py
│   │       __init__.py
│   │
│   ├───static
│   │   └───projectsApp
│   │       ├───CSS
│   │       │       project.css
│   │       │
│   │       └───JS
│   │               project.js
│   │
│   └───templates
│       └───projectsApp
│           └───Html
│                   project.html
│                   test.html
│    
└───Task_management
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
```


</details>

## Установка
1)	Установить Python 3.11
2)	Скачать проект и перейти к нему
3)	Установить все необходимые дополнения командой pip install -r requirements.txt.
4)	Необходимо подключить базу данных PostgreSQL проекту. Для этого надо в файле Task_management/settings.py настроить подключение в данном фрагменте кода:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<dbname>',
        'USER': 'postgres',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
```
Более подробная инструкция по ссылке:
https://proghunter.ru/articles/django-base-2023-installing-postgresql-in-django

5)	Запустите сервер при помощи команды 
python manage.py runserver
6)	 Перейдите по ссылке, которая появится в консоли
## Загрузка данных
В проекте существует файл data-dump.json, в котором находятся данные для тестирования возможностей веб-приложения.<br>
Данные можно загрузить при помощи команды:
```error
python manage.py loaddata data_dump.json
```
Если возникла ошибка:
```bash
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
```
То нужно перейти в файл: `…\site-packages\django\core\serializers\json.py` (полный путь вы увидите в консоли)  и изменить выделенную строку, как показано на скриншоте  
![2024-08-20_23-09-17](https://github.com/user-attachments/assets/a47e1978-d456-4ad0-837a-d733898df5b2)<br>
После этого повторите команду загрузки данных.

