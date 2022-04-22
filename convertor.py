# @Author: Seyed Mohammad Reza Shahrestani
# @date: 22/04/2022


import re
import requests
from difflib import SequenceMatcher


# Converts the query to a single line
# @params: String
# @return: String
def convertToOneLine(query):
    query = str(query)
    query = query.replace("\n", "")
    return query


# Parses the sentence and splits it into two parts
# Returns -1 if the sentence has more that one '$'
# @params: String
# @return: String, String
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
  

# Removes the predicate from the final sentence
# @params: [Strings: list of labels, String: the predicate], [Strings: the final sentence]
# @return: [Strings: the past of the 'final' sentence that is not in the 'predicate' or 'label']
def removePredicate(label, predicate, final):
  
  finalList = []

  for i in range(len(label)):

    if "$" in predicate:
      x = predicate.lower().replace("$", label[i].lower())
      
    x = x.replace(predicate, "").replace(".", "").replace(",", "")
    x = final[i].lower().replace(x, "")
    finalList.append(x.lower())

  return finalList


# Calculates the similarity between two strings
# @params: String: the first string, String: the second string
# @return: Float: a number between 0 and 1
def similar(a, b):
    a = a.lower()
    b = b.lower()
    return SequenceMatcher(None, a, b).ratio()


# This function calculates the similarity of openai and huggingface with wikidata
# @params: [Strings: wikidata labels], [Strings: openai predictions], [Strings: huggingface predictions]
# @return: [Float: openai scores up to 3 decimals], [Floats: huggingface scores up to 3 decimals]
def calcScore(wikidata, openai, huggingface):
  openaiList = []
  huggingfaceList = []

  for i in range(len(wikidata)):
    openaiList.append(round(similar(wikidata[i], openai[i]),3))
    huggingfaceList.append(round(similar(wikidata[i], huggingface[i]),3))

  return openaiList, huggingfaceList


# msmarco-distilbert-base-tas-b URL
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/msmarco-distilbert-base-tas-b"
# msmarco-distilbert-base-tas-b Token
api_token = "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"
headers = {"Authorization": f"Bearer {api_token}"}


# This function makes a post request to the language model
# @params: Dict: inputs
# @return: Json object
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


# This function puts the parameters into a dictionary
# and sends it to query functions
# @params: String: the source sentence, [Strings: list of sentences to be compared with the source sentence]
# @return: Json object
def compare(source, sentences):
    data = query(
    {
        "inputs": {
            "source_sentence": source,
            "sentences": sentences
        }
    })
    return data


# This function pairs the sentences of the language models, then sends it to the comapre function
# along with the source sentence
# @params: [Strings: list of the source sentences], [[LM1: String: sentences], [LM2: String: sentences], ...]
# @return: [Float: final scores]
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