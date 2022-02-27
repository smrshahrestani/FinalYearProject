

from hashlib import new
import json

import requests

API_TOKEN = "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"

headers = {"Authorization": "Bearer " + API_TOKEN}
API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"

def query2(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

data = query2({"inputs": "The answer to the universe is [MASK]."})


for i in range(len(data)):
    print "row", data[i]

newlist = sorted(data, key=lambda k: k["score"], reverse=True) 

print "-"

for i in range(len(newlist)):
    print "row", newlist[i]

print newlist[0].get("sequence")

