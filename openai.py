# @Author: Seyed Mohammad Reza Shahrestani
# @date: 22/04/2022


import requests

# OpenAi URL
completionURL = "https://api.openai.com/v1/engines/text-davinci-001/completions"

# API Token for authentication
id= "Bearer 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"


# This function gets the data from the API endpoint and returns the result
# @params: String: a sentence to be sent to LM
# @return: Strign: the language models response
def complete(sentence):
  json = {
    "prompt": sentence,
    "max_tokens": 5
  }

  req = requests.post(completionURL, headers={'Authorization': id},json = json)
  
  finalText = req.json().get("choices")[0].get("text").replace("\n", "")
  return sentence + finalText