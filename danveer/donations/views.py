from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomerRegistrationForm, DonateItemForm, RequestDonationForm, ChatMessageForm
from .models import DonatedItem, DonationRequest, Donation, ChatMessage, Customer
from django.db.models import Q

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
@login_required
def profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)

# Confirm Donation Page
def confirm(request):
    return render(request, 'confirmation.html')

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
    #Need to create the context dictionary so as to be able to use the variables to be displayed from db
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

#Chat page logic
@login_required
def chat(request, receiver_id):
    receiver = Customer.objects.get(id=receiver_id)
    sender = request.user
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.sender = sender
            chat_message.receiver = receiver
            chat_message.save()
            return redirect('chat', receiver_id=receiver.id)

    else:
        form = ChatMessageForm()

    messages = ChatMessage.objects.filter(
        (Q(sender=sender) & Q(receiver=receiver)) |
        (Q(sender=receiver) & Q(receiver=sender))
    ).order_by('timestamp')

    context = {
        'form': form,
        'messages': messages,
        'receiver': receiver,
    }
    return render(request, 'chat.html', context)

@login_required
def user_chats(request):
    user = request.user  # request.user is already a Customer instance
    sent_chats = ChatMessage.objects.filter(sender=user).values('receiver').distinct()
    received_chats = ChatMessage.objects.filter(receiver=user).values('sender').distinct()

    chat_partners = set()
    for chat in sent_chats:
        chat_partners.add(chat['receiver'])
    for chat in received_chats:
        chat_partners.add(chat['sender'])

    chat_partners = Customer.objects.filter(id__in=chat_partners)
    
    context = {
        'chat_partners': chat_partners,
    }
    return render(request, 'user_chats.html', context)

# Admin Page
def admin(request):
    return render(request, 'admin.html')