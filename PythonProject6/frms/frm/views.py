from django.shortcuts import render
from .form import StuForm
# Create your views here.


def index(request):
    stud=StuForm()

    retuen render(request,'index.html')
