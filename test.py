import openai
import huggingface

from SPARQLWrapper import SPARQLWrapper, JSON

q = ('SELECT DISTINCT ?city WHERE {?city a <http://dbpedia.org/ontology/City> .} LIMIT 5')
dbpedia = 'http://dbpedia.org/sparql'
wikidata = 'https://query.wikidata.org/sparql'

sparql = SPARQLWrapper(wikidata)


city = 'SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q7930989. SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }}LIMIT 5'
country = 'SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q6256. SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }}LIMIT 5'
sparql.setQuery(country)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

predicate = " has the highest rate of "


#for wikidata
for result in results["results"]["bindings"]:
    sentence = result.get("itemLabel").get("value") + " " + predicate

    aianswer = openai.complete(sentence)
    print sentence , aianswer
    print("--------------------------------")
    hanswer = huggingface.complete(sentence)
    print hanswer
    print "==="
    #print(result["label"]["value"])


# # for dbpedia
# for result in results["results"]["bindings"]:
#     print result.get("city").get("value")


