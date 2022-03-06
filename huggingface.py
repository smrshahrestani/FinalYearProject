

from hashlib import new
import json
from operator import indexOf

import requests

API_TOKEN = "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"

headers = {"Authorization": "Bearer " + API_TOKEN}
API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"

def query2(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


input = "this is "

input = "The Capital of Iran is "
input = "Paris is the city of "
input = "why is this "
input = "Tehran is located in "
input = "the capital of England is "




# for i in range(len(data)):
#     print "row", data[i]


# print "-"

# for i in range(len(newlist)):
#     print "row", newlist[i]




def complete(sentence):
    data = query2({"inputs": sentence + " [MASK]."})
    newlist = sorted(data, key=lambda k: k["score"], reverse=True) 
    final = newlist[0].get("sequence")
    return final


print complete(input)