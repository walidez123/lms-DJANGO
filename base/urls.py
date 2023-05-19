from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='main'),
    path('update/<book_id>',update , name='update-book'),
    path('delete/<book_id>',delete , name='delete-book'),
    
    path('books',books ,name='books'),
]
