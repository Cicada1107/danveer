# Generated by Django 5.1.4 on 2025-01-03 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_remove_donation_amount_remove_donation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donateditem',
            name='img',
            field=models.ImageField(blank=True, default='images/default_item_img.png', upload_to=''),
        ),
    ]