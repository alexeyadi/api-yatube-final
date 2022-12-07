# Social Media Network Yatube with API
### Description
Social Media Network with possability write comments, following to authors. Project have API for create users, posts and get other information about posts.
It's my learning project. Here I studied Django and DRF. I use CRUD for other entities. I lernt serializers and deserializers.
### Technology
- Python 3.7
- Django 2.2.19
- Django Rest Framework 3.12.4
- Git 2.37.0.windows.1
- Djoser and JWT Token Auth
### Setup project in dev-mode
- For clone from github use:
```
git clone *code_project*
```
- Setup and activate virtual envirement:
```
python -m venv venv
source venv/scripts/activate
```
- Setup Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
``` 
- Inside folder with file manage.py perform command:
```
python manage.py runserver
```
### Requests to API:
- All posts (use GET):
```
http://127.0.0.1:8000/api/v1/posts/
```
- Create post (use POST):
```
http://127.0.0.1:8000/api/v1/posts/
```
All requests:
```
http://127.0.0.1:8000/redoc/
```
### Авторы
[Aleksei Adishchev](https://github.com/alexeyadi/)
