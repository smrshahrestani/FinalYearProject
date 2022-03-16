from itertools import count
from SPARQLWrapper import SPARQLWrapper, JSON


dbpedia = 'http://dbpedia.org/sparql'
wikidata = 'https://query.wikidata.org/sparql'



q = ('SELECT DISTINCT ?city WHERE {?city a <http://dbpedia.org/ontology/City> .} LIMIT 5')
city = 'SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q7930989. SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }}LIMIT 5'
country = 'SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q6256. SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }}LIMIT 5'

river = """
SELECT ?river ?riverLabel ?location
WHERE
{
  ?river wdt:P31/wdt:P279* wd:Q355304;
         wdt:P30 wd:Q51.
  OPTIONAL { ?river wdt:P625 ?location. }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}LIMIT 5"""


capitals= """SELECT DISTINCT ?item ?itemLabel WHERE {
      ?item p:P279 ?statement0.
      ?statement0 (ps:P279/(wdt:P279*)) wd:Q7930989.
      ?item p:P279 ?statement1.
      ?statement1 (ps:P279/(wdt:P279*)) wd:Q5119.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
}"""


# returns the lables
def findLabels(query):
    values = []
    # print query
    for i in query:
        for key in i:
            if "Label" in key:
                values.append(i.get(key).get("value"))
    return values

# returns the lables
def findDescriptions(query):
    values = []
    # print query
    for i in query:
        for key in i:
            if "Description" in key:
                values.append(i.get(key).get("value"))
    return values

def makeQuery(server, query):
    if server == "wikidata": server = wikidata
    elif server == "dbpedia": server = dbpedia
    else: server = server
    sparql = SPARQLWrapper(server)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results["results"]["bindings"]

def getLabels(server, query):
    return findLabels(makeQuery(server, query))

def getDescriptions(server, query):
    return findDescriptions(makeQuery(server, query))

def getData(server, query):
    query = makeQuery(server, query)
    label = findLabels(query)
    description = findDescriptions(query)
    return label, description



# print (getLabels(wikidata, city)) # output: [u'Moscow', u'Saint Petersburg', u'Abakan', u'Novosibirsk', u'Yekaterinburg']
# print getLabels(wikidata, capitals # output : [u'Q257391', u'Q377283', u'Q1557068', u'Q2324785', u'Q2912045', u'Q3147563', u'Q4442912', u'Q11271835', u'Q12031379', u'Q14770218', u'Q15840617', u'Q21518270', u'Q34843301', u'Q65589340', u'Q104600084', u'Q105742469', u'Q105742483', u'Q105742499', u'Q107566885', u'Q108178728', u'Q14784328', u'Q21507383', u'Q55737404']
# print findLabels(query(wikidata,city))