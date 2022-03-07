


import openai
import huggingface
import convertor
import query as queryMaker



q = """
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

humans = """select distinct ?item ?itemLabel ?itemDescription ?sitelinks where {
    ?item wdt:P31 wd:Q5;  # Any instance of a human.
          wdt:P19/wdt:P131* wd:Q60;  #  Who was born in any value (eg. a hospital)
# that has the property of 'administrative area of' New York City or New York City itself.
             wikibase:sitelinks ?sitelinks.
   
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en,nl" }
}LIMIT 5 """

city = 'SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q7930989. SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }}LIMIT 5'

mountains = '''SELECT ?elevation ?item ?itemLabel ?itemDescription ?coord
WHERE
{
  ?item wdt:P2044 ?elevation .
  filter(?elevation > 8000)
  ?item wdt:P625 ?coord .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}LIMIT 10'''


musicians = '''select distinct ?item ?itemLabel ?itemDescription where {
    ?item wdt:P106/wdt:P279* wd:Q639669 .
    ?item wdt:P19/wdt:P131* wd:Q34370 .
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en,nl" }
}LIMIT 10'''


predicate = ' that is located in '


def magic(server, query):
    listOfVariables = queryMaker.getLabels(server, query)
    listOfDescriptions = queryMaker.getDescriptions(server, query)


    for i in range(len(listOfVariables)):
        if len(listOfDescriptions) is  not 0 : sentance = listOfVariables[i] + " is a " + listOfDescriptions[i]
        else : sentance = listOfVariables[i]
        print "open ai: ",openai.complete(sentance + predicate)
        print "hug: ",huggingface.complete(sentance + predicate)

        print "----" * 10

magic('wikidata', musicians)

