from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')
