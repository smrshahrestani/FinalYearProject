
import huggingface
import openai
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


predicate = ' is located in '


def get(server, query, before='', after=''):
    listOfVariables = queryMaker.getData(server,query)[0]
    listOfDescriptions = queryMaker.getData(server,query)[1]

    openaiList = []
    huggingfaceList = []


    for i in range(len(listOfVariables)):
        if len(listOfDescriptions) != 0 : sentance = listOfVariables[i] + ", " + listOfDescriptions[i]
        else : sentance = listOfVariables[i]
        openaiList.append(openai.complete(before + sentance + after))
        huggingfaceList.append(openai.complete(before + sentance + after))

        print ("open ai:", openaiList[i])
        print ("H face:", huggingfaceList[i])

        print ("----" * 10)

    return openaiList, huggingfaceList, listOfVariables, listOfDescriptions

# get('wikidata', city, predicate)



def magic(server, query, predicate):


  # print("server:", server)
  # print("query:", query)
  # print("predicate:", predicate)

  res = convertor.parse(predicate)
  if res == -1: return res
  elif res == 0: return get(server, query, predicate)
  else:
    # print("before", res[0]) 
    # print("after", res[1]) 
    return get(server, query, res[0], res[1])