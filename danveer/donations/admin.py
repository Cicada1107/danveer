from django.contrib import admin
from .models import Donation, Beneficiary, Donor

# Register your models here.
admin.site.register(Donor)
admin.site.register(Beneficiary)
admin.site.register(Donation)