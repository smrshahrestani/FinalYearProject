# @Author: Seyed Mohammad Reza Shahrestani
# @date: 22/04/2022


import requests


# The URLs of the SPARQL endpoints 
dbpedia = 'http://dbpedia.org/sparql'
wikidata = 'https://query.wikidata.org/sparql'


# This function finds the 'Labels'
# It can find multiple label
# @params: [Dictionary: the query result from the endpoints]
# @return: [labels], [[values in label 1],[values in label 2], ...]
def findLabelsUpdated(query):

    keys = []
    values = []

    for i in query:
        for key in i:
            if "Label" in key:
                if key not in keys:
                    keys.append(key)

    for j in range(len(keys)):
        x = []
        for i in query:
            for key in i:
                if "Label" in key:
                    if keys[j] is key:
                        x.append(i.get(key).get("value"))

        values.append(x)

    return keys, values

# This function finds the 'Description' in the query result
# @params: [Dictionary: the query result from the endpoints]
# @return: [String: the descriptions]
def findDescriptions(query):
    values = []
    # print query
    for i in query:
        for key in i:
            if "Description" in key:
                values.append(i.get(key).get("value"))
    print(values)
    return values


# This function makes the query using a HTTP GET method
# @params: String: name of the server, String: the query
# @return: Json object: result of the query
def makeQuery(server, query):
    if server == "wikidata": server = wikidata
    elif server == "dbpedia": server = dbpedia
    else: server = server

    # An optional field to be added
    # use for authentication 
    headers = {}
    r = requests.get(server, headers=headers, params = {'format': 'json', 'query': query})
    data = r.json()["results"]["bindings"]
    return data


# This is a getter function for finding the labels in a query
# First queries the query, then finds the labels
# @params: String: name of the server, String: the query
# @return: [labels], [[values in label 1],[values in label 2], ...]
def getLabels(server, query):
    return findLabelsUpdated(makeQuery(server, query))


# This is a getter function for finding the descriptions in a query
# First queries the query, then finds the descriptions
# @params: String: name of the server, String: the query
# @return: [String: the descriptions]
def getDescriptions(server, query):
    return findDescriptions(makeQuery(server, query))


# This function queries the data from the server and finds the labels and descriptions if it has one
# Then returns the label and description each as a separate list
# @params: String: name of the server, String: the query
# @return: [String: the labels], [Strings: the descriptions]
def getData(server, query):
    print("Querying From Database, Please be patient...")
    query = makeQuery(server, query)
    label = findLabelsUpdated(query)
    description = findDescriptions(query)
    return label, description