# htmx_crud
## Описание:

Базовое CRUD-приложение для ознакомления с возможностями HTMX.

### Пример:
![alt text](https://i.postimg.cc/WjNJJzxW/example.png)

### Стек технологий:
* Python 3.10
* Django 4.2
* HTMX
* Bootstrap 5

### Установка:

1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:svtplv/htmx_crud.git
```

2. Cоздать и активировать виртуальное окружение:
* Linux/macOS:
```
python3 -m venv venv
source venv/bin/activate
```
* Windows:
```
python -m venv venv
source env/scripts/activate
```

3. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

4. Выполнить миграции:
```
python manage.py migrate
```

5. Запустить проект:
```
python manage.py runserver
```

### Авторы:
[Святослав Поляков](https://github.com/svtplv)