# Generated by Django 5.1.2 on 2025-02-23 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0014_alter_cars_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='picture',
            field=models.ImageField(blank=True, default='cars/cars_photo/default.jpg', null=True, upload_to='cars/cars_photo'),
        ),
    ]
