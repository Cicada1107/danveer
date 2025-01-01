from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=11, choices=[('donor', 'Donor'), ('beneficiary', 'Beneficiary/NGO')], blank=False, null=False)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.username



class Donation(models.Model):
    donor = models.ForeignKey(Customer, limit_choices_to={'user_type': 'donor'}, related_name='donations_given', on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Customer, limit_choices_to={'user_type': 'beneficiary'}, related_name='donations_received', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    pending = models.BooleanField(default=True)

    def __str__(self):
        return f"Donation of {self.amount} from {self.donor} to {self.beneficiary}"