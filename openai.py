


# import os
# import openai

# openai.organization = "org-SKRaZjElzOCua6C1uGLzStHa"
# openai.api_key = os.getenv("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")
# openai.Engine.list()      



import requests
import json


completionURL = "https://api.openai.com/v1/engines/text-davinci-001/completions"
id= "Bearer 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"

sentence = "The Capital of Iran is "


json = {
  "prompt": sentence,
  "max_tokens": 5
}


xx = requests.post(completionURL, headers={'Authorization': id},json = json)
print xx.json()


finalText = xx.json().get("choices")[0].get("text").replace("\n", "")
print sentence + finalText

