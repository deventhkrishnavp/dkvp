from django.shortcuts import render
from django.http import HttpRequest
from .models import Items

# Create your views here.
def index(request):
    shopping = Items.objects.all()
    return render(request,'index.html',{'shopping':shopping})
