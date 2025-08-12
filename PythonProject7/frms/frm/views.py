from django.shortcuts import render
from .forms import StuForm
# Create your views here.


def index(request):
    stud=StuForm

    return render(request,'index.html')
