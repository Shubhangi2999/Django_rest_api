# Django_rest_api

Pre-requisites:
  Python3, pip
  
  
Install 

  1- django

  2- djangorestframework

  3- django-cors-headers

  
After installing the above dependencies, through terminal go to the project directory and run these commands:

  1- python manage.py makemigrations

  2- python manage.py migrate 

  3- python manage.py runserver //to start the server

Now, open localhost:8000/webapp/api/partners in a browser.

POST data in this format:

    {
      "f_name": "abc",
      "l_name": "xyz",
      "email": "xyz@gmail.com",
      "contact": "8313115029",
      "age": "21",
    }
