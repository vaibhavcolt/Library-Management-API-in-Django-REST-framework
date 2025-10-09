***Step-by-Step: Document Your API with Postman***

**1.Open Postman and Create a New Collection**
Launch Postman

Click "Collections" → "New Collection"

Name it something like Library API or Django Backend

**2.Add API Requests to the Collection**
For each endpoint in your Django API (e.g., /api/books/, /api/register/, /api/login/):

Example: Add Book (POST)

Method: POST

URL: http://127.0.0.1:8000/api/register/


Some api are protected so there require authorization using *username* &  *password*.

*After authorization a token will be generated, tokens allow clients to prove identity without sending a username and password on every request.*

json
Authorization: Token your_token_here(like this 647be37deca15e190257dfcab4761818578a233e)
Body (raw JSON):

json:  {

  "name": "The Alchemist",
  "author": "Paulo Coelho"
  
}

Repeat this for:

GET /api/books/

POST /api/register/

POST /api/login/


**3.Test Each Request**
Click Send to verify each request works


<img width="1236" height="798" alt="erDaigram" src="https://github.com/user-attachments/assets/bec777ba-cc57-4670-be2f-28151af814a6" alt="er diagram"/>





***#Save the request to your collection***

**1.Install Python & Virtual Environment**

Make sure Python is installed (recommended: Python 3.10+)

python --version

**2.Install Django and Django REST Framework**

pip install django djangorestframework

I am using MySQL so to use and make connection :

pip install mysqlclient

**3.Create Django Project**

#How i created project

django-admin startproject myproject

cd myproject

**4.Create Django App**

#How to create app

python manage.py startapp api

Add 'rest_framework' and 'api' to INSTALLED_APPS in myproject/settings.py:

setting.py

INSTALLED_APPS = [
    ...
    
    'rest_framework',
    
    'api',
    
]

**5.Create Models, Serializers, and Views**

Define your models in api/models.py, then run:

python manage.py makemigrations

python manage.py migrate

**6.Set Up URLs**

In api/urls.py:

In myproject/urls.py:

python

from django.urls import path, include

urlpatterns = [

    path('api/', include('api.urls')),
    
]

**7.Run Development Server**

python manage.py runserver

Visit: http://127.0.0.1:8000/api/
