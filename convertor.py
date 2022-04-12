
from cmath import pi
from itertools import count
from os import PRIO_PGRP
import re


def convertToOneLine(query):
    query = str(query)
    query = query.replace("\n", "")
    return query


query = """

SELECT ?river ?riverLabel ?location
WHERE
{
  ?river wdt:P31/wdt:P279* wd:Q355304;
         wdt:P30 wd:Q51.
  OPTIONAL { ?river wdt:P625 ?location. }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}LIMIT 10
"""

# print (convertToOneLine(query))


# Tokenize
def parse(data):
  before, after = [], []
  if "$" not in data:
    return 0
  else:
    if data.count("$") > 1:
      return -1
    else:
      data = data.split("$")
      before = data[0]
      after = data[1]
      return before, after
  


res0 = ['The most important city of Kenya is Nairobi', 'The most important city of Ethiopia is Addis Ab', 'The most important city of Ghana is The most important', 'The most important city of France is Paris', 'The most important city of United Kingdom is The most important', "The most important city of People's Republic of China is The most important", 'The most important city of Brazil is The most important', 'The most important city of Russia is Moscow', 'The most important city of Canada is The most important', 'The most important city of Japan is Tokyo.']
res1= ['The most important city of Kenya is Nairobi', 'The most important city of Ethiopia is The most important', 'The most important city of Ghana is The most important', 'The most important city of France is Paris', 'The most important city of United Kingdom is The most important', "The most important city of People's Republic of China is The most important", 'The most important city of Brazil is The most important', 'The most important city of Russia is Moscow', 'The most important city of Canada is There is no', 'The most important city of Japan is Tokyo.']
label1 = ['Kenya', 'Ethiopia', 'Ghana', 'France', 'United Kingdom', "People's Republic of China", 'Brazil', 'Russia', 'Canada', 'Japan']
predicate = "The most important city of $ is "
res2 = ['Kenya', 'Ethiopia', 'Ghana', 'France', 'United Kingdom', "People's Republic of China", 'Brazil', 'Russia', 'Canada', 'Japan']


def removePredicate(label, predicate, final):
  finalList = []
  
  for i in range(len(label)):
    if "$" in predicate:
      x = final[i].replace(label[i], "$").replace(predicate, "").replace(".", "").replace(",", "")
      finalList.append(x)
    else:
      x = final[i].replace(label[i], "").replace(predicate, "").replace(".", "").replace(",", "")
      finalList.append(x)

  return finalList

# removePredicate(label1, predicate, res0


# ----------------------------------------------------------------

from difflib import SequenceMatcher

def similar(a, b):
    a = a.lower()
    b = b.lower()
    return SequenceMatcher(None, a, b).ratio()



o = ['Nairobi', 'Addis Ab', 'The Capital City', 'Paris', 'London', ' Beijing.', 'The capital city', 'Moscow', 'Ottawa', 'Tokyo']
h = ['Nairobi', 'It is officially', 'The capital city', 'Paris.', 'The capital city', 'Beijing', 'Rio de', 'Moscow.', 'Ottawa,', 'Bengaluru']
w = ['Nairobi', 'Addis Ababa', 'Accra', 'Paris', 'London', 'Beijing', 'Brasília', 'Moscow', 'Ottawa', 'Tokyo']





def calcScore(wikidata, openai, huggingface):
  openaiList = []
  huggingfaceList = []

  for i in range(len(wikidata)):
    openaiList.append(round(similar(wikidata[i], openai[i]),3))
    huggingfaceList.append(round(similar(wikidata[i], huggingface[i]),3))


  return openaiList, huggingfaceList






import json
import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/msmarco-distilbert-base-tas-b"
api_token = "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"
headers = {"Authorization": f"Bearer {api_token}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def compare(source, sentences):

    data = query(
    {
        "inputs": {
            "source_sentence": source,
            "sentences": sentences
        }
    })
    print("this is data: ", data)
    return data

def getScore(source, sentences):
    pairScore = []
    for j in range(len(source)):
      a = []
      for i in sentences:
        a.append(i[j])
      pairScore.append(compare(source[j], a))
    
    final = []
    for j in range(len(pairScore[0])):
      lmScore = []
      for i in pairScore:
        lmScore.append(i[j])
      final.append(lmScore)
    return final



# openai = ['Nairobi', 'Addis Ab', 'The capital of', 'Paris', 'London', 'The capital of', 'Brasí', 'Moscow', 'Ottawa', 'Tokyo']
# hface = ['Nairobi', 'Addis Ab', 'The capital city', 'Paris', 'London', 'Beijing', 'Brasí', 'Moscow', 'Ottawa', 'Tokyo']
# w = ['Nairobi', 'Addis Ababa', 'Accra', 'Paris', 'London', 'Beijing', 'Brasília', 'Moscow', 'Ottawa', 'Tokyo']
# all = [openai, hface]
# q = getScore(w,all)


# compare_score_api = [round(x,3) for x in q[0]]
# print('compare the score: ', compare_score_api)