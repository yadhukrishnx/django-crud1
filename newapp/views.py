from django.shortcuts import render

# Create your views here.
from .models import Book

def createbook(request):
    books=Book.objects.all()
    if request.method=='POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        
        book=Book(title=title,price=price)
        
        book.save()
    return render(request,'index.html',{'books':books})

def detailedview(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'detailedview.html',{'book':book})