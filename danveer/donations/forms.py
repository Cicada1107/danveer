from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm

class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    user_type = forms.ChoiceField(
        choices = [('donor', 'Donor'), ('beneficiary', 'Beneficiary/NGO')],
        required = True,
        widget=forms.Select(attrs={'class': 'form control'})
    )
    location = forms.CharField(max_length=200, required=True)

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2', 'user_type', 'location']