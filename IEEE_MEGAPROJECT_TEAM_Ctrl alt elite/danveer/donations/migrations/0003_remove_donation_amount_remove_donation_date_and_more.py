# Generated by Django 5.1.4 on 2025-01-02 17:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_remove_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='date',
        ),
        migrations.AlterField(
            model_name='customer',
            name='location',
            field=models.CharField(help_text='Enter the location of the user', max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user_type',
            field=models.CharField(choices=[('donor', 'Donor'), ('beneficiary', 'Beneficiary/NGO')], help_text='Select the role of the user (Donor or Beneficiary)', max_length=11, verbose_name='User Role'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(limit_choices_to={'user_type': 'donor'}, on_delete=django.db.models.deletion.CASCADE, related_name='donations_donated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DonatedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('food', 'Food'), ('medicines', 'Medicines'), ('educational', 'Education Supplies'), ('furniture', 'Furniture'), ('electronics', 'Electronic Devices'), ('toys', 'Toys'), ('other', 'Other')], max_length=50)),
                ('item_description', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField(blank=True, help_text='Enter quantity if applicable', null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('claimed', models.BooleanField(default=False)),
                ('donor', models.ForeignKey(limit_choices_to={'user_type': 'donor'}, on_delete=django.db.models.deletion.CASCADE, related_name='donated_items', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='donation',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donations.donateditem'),
        ),
        migrations.CreateModel(
            name='DonationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('food', 'Food'), ('medicines', 'Medicines'), ('educational', 'Education Supplies'), ('furniture', 'Furniture'), ('electronics', 'Electronic Devices'), ('toys', 'Toys'), ('other', 'Other')], max_length=50)),
                ('item_description', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField(blank=True, help_text='Enter quantity if applicable', null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('received', models.BooleanField(default=False)),
                ('beneficiary', models.ForeignKey(limit_choices_to={'user_type': 'beneficiary'}, on_delete=django.db.models.deletion.CASCADE, related_name='donations_requested', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
