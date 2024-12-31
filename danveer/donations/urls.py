from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.login, name='login'),  # Login page
    path('profile/', views.profile, name='profile'),  # Profile page
    path('donation/', views.donation, name='donation'),  # Donation page
    path('confirm/', views.confirm, name='confirm'),  # Confirm page
    path('request-donation/', views.request_donation, name='request_donation'),  # Request donation page
    path('explore/', views.explore, name='explore'),  # Explore page
    path('admin/', views.admin, name='admin'),  # Admin page
]