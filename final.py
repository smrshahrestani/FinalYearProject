


import openai
import huggingface
import convertor
import makeQuery



query = """
SELECT DISTINCT ?item ?itemLabel WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
  {
    SELECT DISTINCT ?item WHERE {
      ?item p:P279 ?statement0.
      ?statement0 (ps:P279/(wdt:P279*)) wd:Q7930989.
      ?item p:P279 ?statement1.
      ?statement1 (ps:P279/(wdt:P279*)) wd:Q5119.
    }
    LIMIT 5
  }
}"""
predicate = ' city is the capital of  '


listOfVariables = makeQuery.getLabels('wikidata', query)


for i in listOfVariables:
    print "open ai: ",openai.complete(i + predicate)
    print "hug: ",huggingface.complete(i + predicate)