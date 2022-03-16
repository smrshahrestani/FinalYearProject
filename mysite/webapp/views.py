from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    # x1 = request.POST['']
    x = 1
    x= 2
    return render(request, 'index.html', {'name':'Mohammad'})

def query(request):
    input1 = request.POST['query']
    input2 = request.POST['endpoint']

    return render(request, 'results.html', {"query": input1, "server": "test"})


