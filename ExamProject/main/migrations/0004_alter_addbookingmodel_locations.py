# Generated by Django 3.2.20 on 2023-07-30 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_addbookingmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbookingmodel',
            name='locations',
            field=models.CharField(max_length=50),
        ),
    ]
