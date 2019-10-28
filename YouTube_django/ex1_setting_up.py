#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=Z4D3M-NSN58&list=PLzMcBGfZo4-kQkZp-j9PNyKq7Yw5VYjq9

In command line, from the working dir of "/Users/cay1sgp/Documents/GitHub/learning_python/",
first create a sub-folder eg. YouTube_django/
Then run the cmd django-admin to create the new site template.
$ django-admin startproject mysite

Then change dir into the mysite folder.
$ cd mysite
$ python manage.py runserver
Then launch browser to http://127.0.0.1:8000 to see the default django success page.

Or if you want to start the webserver on a different port of 8082,
$ python manage.py runserver 8082
Then launch browser to http://127.0.0.1:8082 to see page.

Next, create a main sub-folder for the app.
$ python manage.py startapp main
"""
