from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(response):    # The document root of the web server.
    return HttpResponse("<h1>tech with caven!</h1>")


def v1(response):  # Creating a sub-page.
    return HttpResponse("<h1>view 1!</h>")
