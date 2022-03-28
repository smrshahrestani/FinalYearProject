
import requests
import json


completionURL = "https://api.openai.com/v1/engines/text-davinci-001/completions"
old_id= "Bearer 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"
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

# print (complete(sentence))

