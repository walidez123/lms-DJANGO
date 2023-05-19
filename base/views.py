from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.db.models import Sum

# views.py

def index(request):
    category_id = request.GET.get('category')  # Get the selected category from the request parameters
    statue_filter = request.GET.get('statue')  # Get the selected statue filter from the request parameters
    search_name = request.GET.get('search_name')  # Get the search keyword from the request parameters

    books = Book.objects.all()

    if category_id:
        books = books.filter(book_category_id=category_id)

    if statue_filter:
        books = books.filter(statue=statue_filter)

    if search_name:
        # Filter books based on title or author containing the search keyword (case-insensitive)
        books = books.filter(
            Q(title__icontains=search_name) |
            Q(author__icontains=search_name)
        )

    categorys = Category.objects.all()
    forms = BookForm()

    if request.method == "POST":
        forms = BookForm(request.POST, request.FILES)
        catforms = CategoryForm(request.POST)
        if forms.is_valid():
            forms.save()
        if catforms.is_valid():
            catforms.save()
        return redirect('/')
    total_price = Book.objects.aggregate(total=Sum('price'))['total']

    context = {
        'books': books,
        'categorys': categorys,
        'form': forms,
        'catform': CategoryForm(),
        'allbooks': Book.objects.filter(available=True).count,
        'sold': Book.objects.filter(statue="sold").count,
        'rented': Book.objects.filter(statue="rented").count,
        'available': Book.objects.filter(statue="available").count,
        'selected_category': int(category_id) if category_id else None,  # Pass the selected category ID to the template
        'selected_statue': statue_filter if statue_filter else None,  # Pass the selected statue filter to the template
        'search_name': search_name,  # Pass the search keyword to the template
        'total_price':total_price
    }

    return render(request, 'pages/index.html', context)





def update(request,book_id):
        book = Book.objects.get(pk = book_id)
        form = BookForm(request.POST or None ,instance=book)
        if form.is_valid():
            form.save()
            return redirect('main')
        
        
        context = {
              'form' :form,
              'book' :book,
              
        }
        return render(request , 'pages/update.html',context)







def delete(request,book_id):
    task = Book.objects.get(pk = book_id)
    task.delete()
    return redirect('/')
def books(request):
    search_name = request.GET.get('search_name')  # Get the search query from the request parameters
    books = Book.objects.all()

    if search_name:
        # Filter books by title or author containing the search query
        books = books.filter(Q(title__icontains=search_name) | Q(author__icontains=search_name))

    context = {
        'books': books,
    }
    return render(request, 'pages/books.html', context)




# Create your views here.
