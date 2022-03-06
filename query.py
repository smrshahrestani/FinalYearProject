from itertools import count
import openai
import huggingface
import convertor

from SPARQLWrapper import SPARQLWrapper, JSON


dbpedia = 'http://dbpedia.org/sparql'
wikidata = 'https://query.wikidata.org/sparql'

sparql = SPARQLWrapper(wikidata)


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


sparql.setQuery(country)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

predicate = " has the highest rate of "



# returns the lables
def findLabels(query):
    values = []
    # print query
    for i in query:
        for key in i:
            if "Label" in key:
                values.append(i.get(key).get("value"))
    return values



print results["results"]["bindings"]

print "---------"

print "List of Labels: ", findLabels(results["results"]["bindings"])