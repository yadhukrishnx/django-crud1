from django.shortcuts import render,redirect

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

def updatebook(request,book_id):
    
    book=Book.objects.get(id=book_id)
    
    if request.method=='POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        
        book.title=title
        book.price=price
        
        book.save()
        
        return redirect('/')
    
    return render(request,'updatebook.html',{'book':book})