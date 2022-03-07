# NOT COMPATABLE WITH PYTHON 3


import sparql

wikidata = 'https://query.wikidata.org/sparql'
# dbpedia = 'http://dbpedia.org/sparql'

# q = ('SELECT DISTINCT ?city WHERE {?city a <http://dbpedia.org/ontology/City> .} LIMIT 10')
# result = sparql.query(dbpedia, q)

# for i in result:
#     print "row: ", i


# print(result.fetchone())


city = 'SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q7930989. SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }}LIMIT 10'



q=('SELECT DISTINCT ?person ?personLabel  WHERE{ ?person wdt:P69 wd:Q160302. ?person wdt:P21 wd:Q6581072. SERVICE wikibase:label {bd:serviceParam wikibase:language "en".}}')

result = sparql.query(wikidata, city)


total= 0

for i in result:
    total +=1
    print "row: ", i


print ("total: ", total)


print ("----")


