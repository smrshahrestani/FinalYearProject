from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    x = 1
    x= 2
    return render(request, 'index.html', {'name':'Mohammad'})