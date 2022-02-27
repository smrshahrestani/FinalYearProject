import sparql

wikidata = 'https://query.wikidata.org/sparql'
# dbpedia = 'http://dbpedia.org/sparql'

# q = ('SELECT DISTINCT ?city WHERE {?city a <http://dbpedia.org/ontology/City> .} LIMIT 10')
# result = sparql.query(dbpedia, q)

# for i in result:
#     print "row: ", i


# print(result.fetchone())







q=('SELECT DISTINCT ?person ?personLabel  WHERE{ ?person wdt:P69 wd:Q160302. ?person wdt:P21 wd:Q6581072. SERVICE wikibase:label {bd:serviceParam wikibase:language "en".}}')
result = sparql.query(wikidata, q)

result2 = sparql.Service(wikidata).query(q)


total= 0

for i in result:
    total +=1
    print ("row: ", i)

for i in result2:
    print ("result2:  ", i)

print ("total: ", total)




