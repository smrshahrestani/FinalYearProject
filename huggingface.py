# huggingface.py

# @Author: Seyed Mohammad Reza Shahrestani
# @date: 22/04/2022


import json
import requests

# bert-base-uncased URL
API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"

# API Token for authentication
API_TOKEN = "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"

headers = {"Authorization": "Bearer " + API_TOKEN}

# This function makes a HTTP POST request to the API endpoint
# @params: Dict: inputs
# @return: Json object
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

# This function gets the data from the API endpoint and returns the result
# @params: String: a sentence to be sent to LM
# @return: Strign: the language models response
def complete(sentence):
    data = query({"inputs": sentence + " [MASK]."})
    newlist = sorted(data, key=lambda k: k["score"], reverse=True) 
    final = newlist[0].get("sequence")
    return final