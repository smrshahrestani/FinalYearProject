

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


input = "the capital of England is "
input = "Tehran is located at "
input = "this is "

input = "Paris is the city of "
input = "why is this "
input = "The Capital of Iran is "


data = query2({"inputs": input + " [MASK]."})


for i in range(len(data)):
    print "row", data[i]

newlist = sorted(data, key=lambda k: k["score"], reverse=True) 

print "-"

for i in range(len(newlist)):
    print "row", newlist[i]

print newlist[0].get("sequence")

