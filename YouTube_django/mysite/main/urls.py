#!/usr/bin/env python3

from django.urls import path
from . import views     # Import the views from the current directory.

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.v1, name="view 1"),   # Creating a sub-page.
]
