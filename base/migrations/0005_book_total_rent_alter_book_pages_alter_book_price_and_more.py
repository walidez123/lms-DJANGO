# Generated by Django 4.2.1 on 2023-05-19 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_category_book_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rent',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='statue',
            field=models.CharField(blank=True, choices=[('available', 'Available'), ('rented', 'Rented'), ('sold', 'Sold')], max_length=50, null=True),
        ),
    ]
