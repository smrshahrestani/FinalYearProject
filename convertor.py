





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

# print convertToOneLine(query)

