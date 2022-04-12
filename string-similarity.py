import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt') # if necessary...


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


print (cosine_sim('a little bird', 'a little bird'))
print (cosine_sim('a little bird', 'a little bird chirps'))
print (cosine_sim('a little bird', 'a big dog barks'))




#  -----
# not reccomended

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


print(similar('a little bird', 'a little bird'))
print (similar('a little bird', 'a little bird chirps'))
print (similar('a little bird', 'a big dog barks'))



#  -------

print("--")
print(similar('the capital of UK is London', 'the capital of UK is Tehran'))
print(similar('the CAPITAL of UK is London', 'the capital of UK is lOnDon'))
print(cosine_sim('the capital of UK is London', 'the capital of UK is Tehran'))
print(cosine_sim('the CAPITAL of UK is London', 'the capital of UK is lOnDon'))


print("--------------------------------")
# -------



import json
import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/msmarco-distilbert-base-tas-b"
api_token = "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"
headers = {"Authorization": f"Bearer {api_token}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def compare(source, sentences):
    data = query(
    {
        "inputs": {
            "source_sentence": source,
            "sentences": sentences
        }
    })
    return data

# print("this is the data from hf: ", data)
## [0.853, 0.981, 0.655]


