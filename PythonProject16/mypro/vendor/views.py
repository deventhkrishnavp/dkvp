from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .form import VendorRegistrationForm, VendorLoginForm
from .models import VendorProfile

def vendor_register(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # ✅ FIXED: Correct creation of VendorProfile
            VendorProfile.objects.create(user=user, business_name=form.cleaned_data['business_name'])
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('vendor_login')
    else:
        form = VendorRegistrationForm()
    return render(request, 'vendor/register.html', {'form': form})

def vendor_login(request):
    if request.method == 'POST':
        form = VendorLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # ✅ Correct use of login()
            return redirect('vendor_dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        form = VendorLoginForm()
    return render(request, 'vendor/login.html', {'form': form})

@login_required
def vendor_dashboard(request):
    profile = VendorProfile.objects.get(user=request.user)
    return render(request, 'vendor/dashboard.html', {'vendor': profile})

def vendor_logout(request):
    logout(request)
    return redirect('vendor_login')


