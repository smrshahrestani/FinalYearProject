
import requests
import json


completionURL = "https://api.openai.com/v1/engines/text-davinci-001/completions"
id= "Bearer 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"

sentence = "The Capital of Iran is "

def complete(sentence):
  json = {
    "prompt": sentence,
    "max_tokens": 5
  }

  req = requests.post(completionURL, headers={'Authorization': id},json = json)
  
  finalText = req.json().get("choices")[0].get("text").replace("\n", "")
  return sentence + finalText

# print complete(sentence)

