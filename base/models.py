from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    BOOK_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('sold', 'Sold'),
    ]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    pages = models.IntegerField()
    book_pic = models.ImageField(upload_to='pics', null=True, blank=True)
    author_pic = models.ImageField(upload_to='pics', null=True, blank=True)
    available = models.BooleanField(default=True)
    statue = models.CharField(max_length=50, choices=BOOK_CHOICES, null=True, blank=True)
    book_category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    total_rent = models.DecimalField(max_digits=5,decimal_places=2, null=True, blank=True)
    def __str__(self):
        return self.title

    
# Create your models here.
