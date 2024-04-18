from django.shortcuts import render
from .models import Book, Project

# Create your views here.
def home(request):
    all_books = Book.objects.all()
    all_projects = Project.objects.all()
    return render(request, 'base\home.html', {'books':all_books, 'projects':all_projects})
