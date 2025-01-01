from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

# Home Page
def home(request):
    return render(request, 'home.html')

# Registration Page
def register(request):
    return render(request, 'registration.html')

# Login Page
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'invalid email or password')
    return render(request, 'login.html')

#logout page
def logout(request):
    return render(request, 'logout.html')

# Profile Page
def profile(request):
    return render(request, 'profile.html')

# Donation Page
def donation(request):
    return render(request, 'donation.html')

# Confirm Donation Page
def confirm(request):
    return render(request, 'confirm.html')

# Request Donation Page
def request_donation(request):
    return render(request, 'request_donation.html')

# Explore Page
def explore(request):
    return render(request, 'explore.html')

# Admin Page
def admin(request):
    return render(request, 'admin.html')