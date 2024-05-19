from django.shortcuts import render

# Create your views here.
from .models import Book

def createbook(request):
    if request.method=='POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        
        book=Book(title=title,price=price)
        
        book.save()
    
    return render(request,'index.html')