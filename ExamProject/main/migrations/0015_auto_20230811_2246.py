# Generated by Django 3.2.20 on 2023-08-11 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20230811_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addbookingmodel',
            name='images',
        ),
        migrations.CreateModel(
            name='BookingImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='user_pictures')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.addbookingmodel')),
            ],
        ),
    ]
