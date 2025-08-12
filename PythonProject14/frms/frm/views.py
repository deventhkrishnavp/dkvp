from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages




# Create your views here.



def index(request):

    return render(request,'index.html')


def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,'successfully login')
            return redirect('destination')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')  # Stay on login page

    return render(request, 'login.html')



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signupp(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        # Check if email already exists
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')

        # Create and save user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')  # Use the correct URL name for your login view

    return render(request, 'signup.html')

