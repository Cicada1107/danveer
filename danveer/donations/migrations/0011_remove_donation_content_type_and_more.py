# Generated by Django 5.1.4 on 2025-01-11 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0010_remove_donation_item_donation_content_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='object_id',
        ),
        migrations.AddField(
            model_name='donation',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donations.donateditem'),
        ),
    ]