from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Map URL /products to the index func.
def index(request):
    return HttpResponse("Hello World")

