from django.shortcuts import render
from django.http import HttpResponse

# # import  
import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/smr/Documents/Kings/BSci/Third_Year/Final Project/Python /FinalYearProject')
import final




# Create your views here.
name = "Seyed"

# A function for loading the index page
def index(request):
    return render(request, 'index.html', {'name':name})

# A function for loading the static page
def stats(request):
    return render(request, 'stats.html')




def query(request):
    query = request.POST['query']
    endpoint = request.POST['endpoint']
    predicate = request.POST['predicate']
    
    # serverAddress = request.POST['endpoint-address']



    # customEndpoint = request.POST['Custom_Endpoint_Address']
    # print (customEndpoint)

    print("endpoint" , endpoint)
    if endpoint == "1": server = "wikidata"
    elif endpoint == "2": server = "dbpedia"
    elif endpoint == "3": server = ""

    results = final.magic(server, query, predicate)
    if results == -1: return HttpResponse("Use of too many '$' in the predicate")

    if results[3] == []: 
        hasDescription = False
        myzip = zip(range(len(results[2])),results[2], results[0], results[1])
    else: 
        hasDescription = True
        myzip = zip(range(len(results[2])),results[2], results[3], results[0], results[1])

    myContext = {
        "name": name,
        "query": query,
        "endpoint": endpoint,
        "predicate": predicate,
        "myzip": myzip,
        "hasDescription": hasDescription,
        }

    return render(request, 'results.html', myContext)

