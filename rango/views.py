from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # creating a view called index
    # each view must return a HttpResponse object
    return HttpResponse ("Rango says hey there partner!")
