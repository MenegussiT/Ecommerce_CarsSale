# Generated by Django 5.1 on 2024-08-28 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_value_alter_car_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='value',
        ),
    ]
