# Generated by Django 3.2.20 on 2023-07-30 18:11

import ExamProject.main.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_addbookingmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3, 'Username must be at least 3 characters')])),
                ('password', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(8, 'Password should contain at least 8 symbols'), ExamProject.main.validators.atleast_one_digit])),
                ('repeatPassword', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='addbookingmodel',
            name='image',
        ),
        migrations.CreateModel(
            name='BookingImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='user_pictures')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.addbookingmodel')),
            ],
        ),
    ]