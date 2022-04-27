# @Author: Seyed Mohammad Reza Shahrestani
# @date: 22/04/2022


from django.shortcuts import render
from django.http import HttpResponse
import os, sys

# Import from parent paths
path = os.path.abspath('.')
sys.path.insert(1, path)
import final 
import data as dataClass
import query as queryMaker
import convertor


# Storing the data globally to be accessed by all methods
data = dataClass.getData()
titles, queries, predicates, answerQueries = data[0], data[1], data[2], data[3]


# A function for loading the playground page
def playground(request):
    print(type(request))
    return render(request, 'playground.html', { "currentPage": "playground"})


# A function for loading the static page
def stats(request):
    myContext = {
        "currentPage": "stats",
        "titles": zip(range(len(titles)),titles),
        "answerQueries": zip(range(len(answerQueries)),answerQueries),
    }

    return render(request, 'stats.html', myContext)


# A function to update the statistic page after applying the changes 
def apply(request):
    dropdown = int(request.POST.get('queryDropDown'))
    myContext = {
        "currentPage": "",
        "titles": zip(range(len(titles)),titles),
        "query": queries[dropdown],
        "answerQuery": answerQueries[dropdown],
        "predicates": predicates[dropdown],
        "dropdown": [dropdown, titles[dropdown]],
    }

    return render(request, 'stats.html', myContext)


# A function to get statistics page data and send it to the language models and show the results back
# and comapres the results with the wikidata answer query
# gives an individual score and an average score for both language models
def statsData(request):
    
    # To keep the data after the pages reloads
    query = request.POST['query']
    predicate = request.POST['predicateText']
    answerQuery = request.POST['answerQuery']
    dropdown = request.POST.get('title')

    # Sends the query and the predicate to the language models and stores the result as list of lists
    results = final.magic("wikidata", query, predicate)

    # Returns an Error page with this message if the user uses more that one '$' 
    if results == -1: return HttpResponse("Use of too many '$' in the predicate")

    # time.sleep(5)
    # Queries the 'answer query' to the wikidata and stores the result as a List of strings
    wikidataResults = queryMaker.getData("wikidata", answerQuery)[0][1][0]

    # Removes the predicate from the LM results
    openaiFinal = convertor.removePredicate(results[2], predicate, results[0])
    huggingFaceFinal = convertor.removePredicate(results[2], predicate, results[1])

    # Compares the openai and hugging face results by sending the results to the hugging face language model
    compare_score_api = convertor.getScore(wikidataResults, [openaiFinal, huggingFaceFinal])
    openaiScore_api = [round(x,3) for x in compare_score_api[0]]
    huggingfaceScore_api = [round(x,3) for x in compare_score_api[1]]

    # Calculating the average score up to 3 decimals
    openaiOveralScore_api = round(sum(openaiScore_api)/len(openaiScore_api),3)
    huggingFaceOveralScore_api = round(sum(huggingfaceScore_api)/len(huggingfaceScore_api),3)

    # Compares the openai and hugging face results using a python library
    openaiScore = convertor.calcScore(wikidataResults, openaiFinal, huggingFaceFinal)[0]
    huggingfaceScore = convertor.calcScore(wikidataResults, openaiFinal, huggingFaceFinal)[1]

    # Calculating the average score up to 3 decimals
    openaiOveralScore = round(sum(openaiScore)/len(openaiScore),3)
    huggingFaceOveralScore = round(sum(huggingfaceScore)/len(huggingfaceScore),3)

    # Checks if the the query has 'description' and stores the result accordingly
    if results[3] == []: 
        hasDescription = False
        myzip = zip(range(len(results[2])),results[2], wikidataResults, results[0], openaiScore, openaiScore_api, results[1], huggingfaceScore, huggingfaceScore_api)
    else: 
        hasDescription = True
        myzip = zip(range(len(results[2])),results[2], results[3], wikidataResults, results[0], openaiScore, openaiScore_api, results[1], huggingfaceScore, huggingfaceScore_api)

    # A dictionary object that stores the necessary variables to send to the html page
    myContext = {
        "currentPage": "stats",
        "titles": zip(range(len(titles)),titles),
        "query": query,
        "answerQuery": answerQuery,
        "predicate": predicate,
        "mydata": "myData",
        "myzip": myzip,
        "hasDescription": hasDescription,
        "openaiOveralScore": openaiOveralScore,
        "huggingFaceOveralScore": huggingFaceOveralScore,
        "openaiOveralScore_api" : openaiOveralScore_api,
        "huggingFaceOveralScore_api": huggingFaceOveralScore_api,
        "dropdown": dropdown,
    }

    # Rendering the html page and sending the results to the page
    return render(request, 'statResults.html', myContext)


# A function to query playground page
def query(request):

    # To keep the data after the pages reloads
    query = request.POST['query']
    endpoint = request.POST['endpoint']
    predicate = request.POST['predicate']

    # Gets the endpoint
    if endpoint == "1": server = "wikidata"
    elif endpoint == "2": server = "dbpedia"
    elif endpoint == "3": server = ""

    # Sends the query and the predicate to the language models and stores the result as list of lists
    results = final.magic(server, query, predicate)

    # Returns an Error page with this message if the user uses more that one '$' 
    if results == -1: return HttpResponse("Use of too many '$' in the predicate")

    # Checks if the the query has 'description' and stores the result accordingly
    if results[3] == []: 
        hasDescription = False
        myzip = zip(range(len(results[2])),results[2], results[0], results[1])
    else: 
        hasDescription = True
        myzip = zip(range(len(results[2])),results[2], results[3], results[0], results[1])

    # A dictionary object that stores the necessary variables to send to the html page
    myContext = {
         "currentPage": "stats",
        "query": query,
        "endpoint": endpoint,
        "predicate": predicate,
        "myzip": myzip,
        "hasDescription": hasDescription,
        }

    # Rendering the html page and sending the results to the page
    return render(request, 'results.html', myContext)