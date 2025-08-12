from django.utils import timezone


from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

from .models import Package


# Create your views here.
def home(request):
    return render(request,'go/home.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        password2 = request.POST.get('password2', '').strip()

        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')

        # Create user
        User.objects.create_user(username=username, password=password, email=email)
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('log')  # change 'log' to your login URL name

    return render(request, 'signup.html')  # show form on GET



def log(request):
    if request.method=="POST":
        username=request.POST.get('username','').strip()
        password= request.POST.get('password', '').strip()
        user=authenticate(password=password,username=username)
        if user is not None:
            login(request,user)
            messages.success(request,'loggedin')
            return redirect('destination')
        else:
            messages.error(request,'tryagain')
            return redirect('log')
    return render(request, 'go/log.html')


def all_package(request):
    today = timezone.now().date()

    # ✅ store the result of the query
    packages = Package.objects.filter(
        is_approved=True
    ).filter(
        Q(expiry_date__isnull=True) | Q(expiry_date__gt=today)
    )

    return render(request, 'destination.html', {'pack': packages, 'title': "All Package"})





def top_packages(request):
    today=timezone.now().date()
    Package.objects.filter(
        is_approved=True,is_top=True
    ).filter(
        Q(expiry_date__isnull=True)|Q(expiry_date__gt=today)
    )
    return render(request, 'destination.html', {'pack': Package, 'title': "Top Package"})

def budget_package(request):
    today=timezone.now().date()
    Package.objects.filter(
        is_approved=True,price__lte=5000
    ).filter(
        Q(expiry_date__isnull=True)|Q(expiry_date__gt=today)
    )
    return render(request, 'destination.html', {'pack': Package, 'title': "Budget Package"})

def package_by_destination(request):
    today=timezone.now().date()
    Package.objects.filter(
        is_approved=True,destination_iexact=package_by_destination

    ).filter(
        Q(expiry_date__isnull=True)|Q(expiry_date__gt=today)
    )
    return render(request, 'destination.html', {'pack': Package, 'title': "Budget Package"})




