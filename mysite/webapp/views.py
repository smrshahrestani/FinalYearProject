from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    # x1 = request.POST['']
    x = 1
    x= 2
    return render(request, 'index.html', {'name':'Mohammad'})

def query(request):
    query = request.POST['query']
    endpoint = request.POST['endpoint']
    print ("this is the endpoint"+endpoint)
    # customEndpoint = request.POST['Custom_Endpoint_Address']
    # print (customEndpoint)

    return render(request, 'results.html', {"query": query, "endpoint": endpoint})


