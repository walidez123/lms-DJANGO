# Generated by Django 4.2.1 on 2023-05-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='statue',
            field=models.CharField(blank=True, choices=[('available', 'available'), ('rented', 'rented'), ('sold', 'sold')], max_length=50, null=True),
        ),
    ]
