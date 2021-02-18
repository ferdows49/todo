from django.shortcuts import render
from .models import Todo

def index(request):
    list = Todo.objects.all()

    return render(request, 'index.html', {'lists': list})