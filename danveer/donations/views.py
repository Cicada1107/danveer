from django.shortcuts import render

# Create your views here.

# Home Page
def home(request):
    return render(request, 'home.html')

# Registration Page
def register(request):
    return render(request, 'registration.html')

# Login Page
def login(request):
    return render(request, 'login.html')

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