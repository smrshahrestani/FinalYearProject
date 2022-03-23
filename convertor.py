

from cmath import pi
from itertools import count
from os import PRIO_PGRP
import re


def convertToOneLine(query):
    query = str(query)
    query = query.replace("\n", "")
    return query


query = """

SELECT ?river ?riverLabel ?location
WHERE
{
  ?river wdt:P31/wdt:P279* wd:Q355304;
         wdt:P30 wd:Q51.
  OPTIONAL { ?river wdt:P625 ?location. }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}LIMIT 10
"""

# print (convertToOneLine(query))


# Tokenize
def parse(data):
  before, after = [], []
  if "$" not in data:
    return 0
  else:
    if data.count("$") > 1:
      return -1
    else:
      data = data.split("$")
      before = data[0]
      after = data[1]
      return before, after



    


