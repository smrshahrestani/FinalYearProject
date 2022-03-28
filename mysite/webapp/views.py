from re import T
from this import d
from django.shortcuts import render
from django.http import HttpResponse

# # import  
import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/smr/Documents/Kings/BSci/Third_Year/Final Project/Python /FinalYearProject')
import final 
import data as dataClass
import query as queryMaker
import convertor



# Create your views here.
name = "Seyed"
data = dataClass.getData()
titles, queries, predicates, answerQueries = data[0], data[1], data[2], data[3]



# A function for loading the index page
def index(request):
    return render(request, 'index.html', {'name':name})

# A function for loading the static page
def stats(request):

    myContext = {
        "name": name,
        "titles": zip(range(len(titles)),titles),
        "answerQueries": zip(range(len(answerQueries)),answerQueries),

    }

    return render(request, 'stats.html', myContext)




def apply(request):

    dropdown = int(request.POST.get('queryDropDown'))

    myContext = {
        "name": name,
        "titles": zip(range(len(titles)),titles),
        "query": queries[dropdown],
        "answerQuery": answerQueries[dropdown],
        "predicates": predicates[dropdown],
        "dropdown": dropdown,

    }
    return render(request, 'stats.html', myContext)


def statsData(request):

    query = request.POST['query']
    predicate = request.POST['predicate']
    answerQuery = request.POST['answerQuery']


    results = final.magic("wikidata", query, predicate)
    if results == -1: return HttpResponse("Use of too many '$' in the predicate")

    wikidataResults = queryMaker.getData("wikidata", answerQuery)[0][1][0]
    
    openaiFinal = convertor.removePredicate(results[2], predicate, results[0])
    huggingFaceFinal = convertor.removePredicate(results[2], predicate, results[1])

    openaiScore = convertor.calcScore(wikidataResults, openaiFinal, huggingFaceFinal)[0]
    huggingfaceScore = convertor.calcScore(wikidataResults, openaiFinal, huggingFaceFinal)[1]

    openaiOveralScore = round(sum(openaiScore)/len(openaiScore),3)
    huggingFaceOveralScore = round(sum(huggingfaceScore)/len(huggingfaceScore),3)

    if results[3] == []: 
        hasDescription = False
        myzip = zip(range(len(results[2])),results[2], wikidataResults, results[0], openaiScore, results[1], huggingfaceScore)
    else: 
        hasDescription = True
        myzip = zip(range(len(results[2])),results[2], results[3], wikidataResults, results[0], openaiScore, results[1], huggingfaceScore)

    myContext = {
        "name": name,
        "titles": zip(range(len(titles)),titles),
        "query": query,
        "answerQuery": answerQuery,
        "predicates": predicate,
        "mydata": "myData",
        "myzip": myzip,
        "hasDescription": hasDescription,
        "openaiOveralScore": openaiOveralScore,
        "huggingFaceOveralScore": huggingFaceOveralScore,
    }

    return render(request, 'statResults.html', myContext)



def query(request):
    query = request.POST['query']
    endpoint = request.POST['endpoint']
    predicate = request.POST['predicate']

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

