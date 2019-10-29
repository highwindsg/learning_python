from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


# Create your views here.

def index(response, name):    # The document root of the web server.
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))


# def v1(response):  # Creating a sub-page.
#     return HttpResponse("<h1>view 1!</h>")
