import requests

url = 'https://query.wikidata.org/sparql'
query = """
PREFIX bd: <http://www.bigdata.com/rdf#> 
PREFIX wd: <http://www.wikidata.org/entity/> 
PREFIX wdt: <http://www.wikidata.org/prop/direct/> 
PREFIX wikibase: <http://wikiba.se/ontology#> 
#added before 2016-10
SELECT DISTINCT ?country ?countryLabel
WHERE
{
  ?country wdt:P31 wd:Q3624078 .
  #not a former country
  FILTER NOT EXISTS {?country wdt:P31 wd:Q3024240}
  #and no an ancient civilisation (needed to exclude ancient Egypt)
  FILTER NOT EXISTS {?country wdt:P31 wd:Q28171280}
  OPTIONAL { ?country wdt:P36 ?capital } .

  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
ORDER BY ?country
LIMIT 10

"""
r = requests.get(url, params = {'format': 'json', 'query': query})
data = r.json()
print(data)


def findLabelsUpdated(query):
    keys = []
    values = []

    # print query
    for i in query:
        for key in i:
            if "Label" in key:
                if key not in keys:
                    keys.append(key)

    for j in range(len(keys)):
        x = []
        for i in query:
            for key in i:
                if "Label" in key:
                    if keys[j] is key:
                        x.append(i.get(key).get("value"))

        values.append(x)

    return keys, values


print(findLabelsUpdated(data["results"]["bindings"]))