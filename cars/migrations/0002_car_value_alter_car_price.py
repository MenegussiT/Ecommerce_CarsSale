# Generated by Django 5.1 on 2024-08-28 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
