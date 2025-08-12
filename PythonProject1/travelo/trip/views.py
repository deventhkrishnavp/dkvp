from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def