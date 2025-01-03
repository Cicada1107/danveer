from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Utility for quantity validation
def validate_quantity(category, quantity):
    if category == 'food' and quantity is None:
        raise ValidationError('Quantity is required for food donations (in kg).')
    if category in ['medicines', 'educational', 'furniture', 'electronics', 'toys'] and quantity is None:
        raise ValidationError('Quantity is required for this category.')
    if category == 'other' and quantity is not None:
        raise ValidationError('Quantity should not be specified for "Other" category.')
    if quantity and quantity <= 0:
        raise ValidationError('Quantity must be a positive integer.')
    

# Create your models here.
class Customer(AbstractUser):
    email = models.EmailField(unique=True)
    user_type = models.CharField(
        max_length=11, 
        choices=[('donor', 'Donor'), ('beneficiary', 'Beneficiary/NGO')], 
        blank=False, 
        null=False, 
        verbose_name='User Role', 
        help_text='Select the role of the user (Donor or Beneficiary)'
    )
    location = models.CharField(
        max_length=200,
        help_text='Enter the location of the user')

    def __str__(self):
        return self.username

    
class DonatedItem(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'), 
        ('medicines', 'Medicines'), 
        ('educational', 'Education Supplies'),
        ('furniture', 'Furniture'), 
        ('electronics', 'Electronic Devices'), 
        ('toys', 'Toys'), 
        ('other', 'Other')
    ]
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50, blank=False, null=False)
    item_description = models.CharField(max_length=100, blank=False, null=False)
    quantity = models.PositiveIntegerField(null=True, blank=True, help_text="Enter quantity if applicable")
    donor = models.ForeignKey(
        Customer, limit_choices_to={'user_type': 'donor'},
        related_name='donated_items',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)
    claimed = models.BooleanField(default=False)
    img = models.ImageField(default='images/default_item_img.png', blank=True)
    
    def clean(self):
        """Custom validation logic for quantity field based on category."""
        validate_quantity(self.category, self.quantity)
        
    def save(self, *args, **kwargs):
        """Ensure clean is called before saving."""
        self.clean()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.item_description} is available for donation from the donor {self.donor}"

    class Meta:
        ordering = ['-date']
        
class DonationRequest(models.Model):
    CATEGORY_CHOICES = DonatedItem.CATEGORY_CHOICES  # Reuse choices
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50, blank=False, null=False)
    item_description = models.CharField(max_length=100, blank=False, null=False)
    quantity = models.PositiveIntegerField(null=True, blank=True, help_text="Enter quantity if applicable")
    beneficiary = models.ForeignKey(Customer, limit_choices_to={'user_type': 'beneficiary'}, related_name='donations_requested', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    received = models.BooleanField(default=False)
    img = models.ImageField(default='images/default_request_img.png', blank=True, help_text='Provide a picture of organization/needy')

    def clean(self):
        """Custom validation logic for quantity field based on category."""
        validate_quantity(self.category, self.quantity)

    def save(self, *args, **kwargs):
        """Ensure clean is called before saving."""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.beneficiary} made the following donation request: {self.item_description}"

class Donation(models.Model):
    donor = models.ForeignKey(Customer, limit_choices_to={'user_type': 'donor'}, related_name='donations_donated', on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Customer, limit_choices_to={'user_type': 'beneficiary'}, related_name='donations_received', on_delete=models.CASCADE)
    item = models.ForeignKey(DonatedItem, on_delete=models.CASCADE, null=True)
    pending = models.BooleanField(default=True)

    def __str__(self):
        return f"Donation of {self.amount} from {self.donor} to {self.beneficiary}"