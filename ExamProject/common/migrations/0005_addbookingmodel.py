# Generated by Django 3.2.20 on 2023-07-30 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_alter_tripbooking_guests'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('name', models.CharField(max_length=50)),
                ('locations', models.TextField(max_length=50)),
                ('guests', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
