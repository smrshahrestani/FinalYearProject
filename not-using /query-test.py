import openai
import huggingface
import convertor

from SPARQLWrapper import SPARQLWrapper, JSON

q = ('SELECT DISTINCT ?city WHERE {?city a <http://dbpedia.org/ontology/City> .} LIMIT 5')
dbpedia = 'http://dbpedia.org/sparql'
wikidata = 'https://query.wikidata.org/sparql'

sparql = SPARQLWrapper(wikidata)


city = 'SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q7930989. SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }}LIMIT 5'
country = 'SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q6256. SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }}LIMIT 5'

river = convertor.convertToOneLine("""
SELECT ?river ?riverLabel ?location
WHERE
{
  ?river wdt:P31/wdt:P279* wd:Q355304;
         wdt:P30 wd:Q51.
  OPTIONAL { ?river wdt:P625 ?location. }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}LIMIT 10""")


sparql.setQuery(river)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

predicate = " has the highest rate of "


#for wikidata
for result in results["results"]["bindings"]:
    sentence = result.get("itemLabel").get("value") + " " + predicate

    aianswer = openai.complete(sentence)
    print (sentence , aianswer)
    print("--------------------------------")
    hanswer = huggingface.complete(sentence)
    print (hanswer)
    print ("===")
    #print(result["label"]["value"])


# # for dbpedia
# for result in results["results"]["bindings"]:
#     print result.get("city").get("value")


