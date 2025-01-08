from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomerRegistrationForm, DonateItemForm, RequestDonationForm
from .models import DonatedItem, DonationRequest, Donation

# Create your views here.

# Home Page
def home(request):
    return render(request, 'home.html')

# Registration Page
def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Login Page
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'login.html')

#Logout functionality
def custom_logout(request):
    logout(request)
    return redirect('home')

# Profile Page
def profile(request):
    return render(request, 'profile.html')

# Confirm Donation Page
def confirm(request):
    return render(request, 'confirm.html')

# Donate Page for Donors
def donate(request):
    if(request.method == 'POST'):
        form = DonateItemForm(request.POST, request.FILES)
        if form.is_valid():
            donated_item = form.save(commit=False)
            donated_item.donor = request.user
            donated_item.save()
            return redirect('home')
    else:
        form = DonateItemForm()
    return render(request, 'donate.html', {'form': form})

# Request Donation Page for NGOs
def request_donation(request):
    if(request.method == 'POST'):
        form = RequestDonationForm(request.POST, request.FILES)
        if form.is_valid():
            requested_item = form.save(commit = False)
            requested_item.beneficiary = request.user
            requested_item.save()
            return redirect('home')
    else:
        form = RequestDonationForm()
    return render(request, 'request_donation.html', {'form': form})

# Explore Page
def explore(request):
    #Need to create the conntext dictionary so as to be able to use the variables to be displayed from db
    unclaimed_donated_items = DonatedItem.objects.filter(claimed=False)
    unreceived_donation_requests = DonationRequest.objects.filter(received=False)
    pending_donations = Donation.objects.filter(pending=True).order_by('-item__date')
    resolved_donations = Donation.objects.filter(pending=False).order_by('item__date')
    context = {
        'unclaimed_donated_items': unclaimed_donated_items,
        'unreceived_donation_requests': unreceived_donation_requests,
        'pending_donations': pending_donations,
        'resolved_donations': resolved_donations,
    }

    return render(request, 'explore.html', context)

# Admin Page
def admin(request):
    return render(request, 'admin.html')