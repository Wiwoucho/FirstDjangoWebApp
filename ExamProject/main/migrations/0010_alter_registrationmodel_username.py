# Generated by Django 3.2.20 on 2023-07-30 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20230730_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(3, 'Username must be at least 3 characters')]),
        ),
    ]
