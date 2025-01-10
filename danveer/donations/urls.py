from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.custom_logout, name='logout'), #Logout page
    path('profile/', views.profile, name='profile'),  # Profile page
    path('donate/', views.donate, name='donate'),  # Donation page for Donor
    path('confirm/', views.confirm, name='confirm'),  # Confirm page
    path('request-donation/', views.request_donation, name='request_donation'),  # Request donation page
    path('explore/', views.explore, name='explore'),  # Explore page
    path('chat/<int:receiver_id>/', views.chat, name='chat'), #Chat page
    path('user-chats/', views.user_chats, name='user_chats'), #Donor's chats
    path('admin/', views.admin, name='admin'),  # Admin page
]