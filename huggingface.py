

from hashlib import new
import json
from operator import indexOf

import requests

API_TOKEN = "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"

headers = {"Authorization": "Bearer " + API_TOKEN}
API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


input = "this is "
input = "The Capital of Iran is "
input = "Paris is the city of "
input = "why is this "
input = "the capital of England is "
input = "Tehran is located in "


# sentence has to be changed to before and after
def complete(sentence):
    data = query({"inputs": sentence + " [MASK]."})
    newlist = sorted(data, key=lambda k: k["score"], reverse=True) 
    final = newlist[0].get("sequence")
    return final


# print (complete(input))
