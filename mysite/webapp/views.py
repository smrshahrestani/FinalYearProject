from re import T
from django.shortcuts import render
from django.http import HttpResponse

# # import  
import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/smr/Documents/Kings/BSci/Third_Year/Final Project/Python /FinalYearProject')
import final 
import data as dataClass
import query as queryClass




# Create your views here.
name = "Seyed"

# A function for loading the index page
def index(request):
    return render(request, 'index.html', {'name':name})

# A function for loading the static page
def stats(request):

    data = dataClass.getData()
    titles, queries, predicates, answerQueries = data[0], data[1], data[2], data[3]
    myContext = {
        "titles": zip(range(len(titles)),titles),
        "queries": zip(range(len(queries)),queries),
        "predicates": zip(range(len(predicates)),predicates),
        "answerQueries": zip(range(len(answerQueries)),answerQueries),

    }

    return render(request, 'stats.html', myContext)


def statsData(request):

    # dropdown = request.POST['dropdown']
    query = request.POST['query']
    predicate = request.POST['predicate']
    answerQuery = request.POST['answerQuery']

    results = final.magic("wikidata", query, predicate)
    if results == -1: return HttpResponse("Use of too many '$' in the predicate")

    openaiScore = [1,2,1,1]
    huggingfaceScore = [2,2,3,3]
    wikidataResults = [2,2,3,2]
    

    if results[3] == []: 
        hasDescription = False
        myzip = zip(range(len(results[2])),results[2], wikidataResults, results[0], openaiScore, results[1], huggingfaceScore)
    else: 
        hasDescription = True
        myzip = zip(range(len(results[2])),results[2], results[3], results[0], results[1])


    data = dataClass.getData()
    titles, queries, predicates, answerQueries = data[0], data[1], data[2], data[3]
    myData = zip(range(len(titles)),titles,queries,predicates, answerQueries) 
    myContext = {
        "name": name,
        "dropdown": "dropdown",
        "query": query, 
        "predicate": predicate,
        "answerQuery": answerQuery,
        "mydata": myData,
        "titles": titles,
        "myzip": myzip,
        "hasDescription": hasDescription
    }
    print("titles:",titles)
    print("queries:",queries)
    print("predicates:",predicates)
    return render(request, 'statResults.html', myContext)



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

