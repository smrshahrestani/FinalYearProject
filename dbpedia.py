import sparql


dbpedia = 'http://dbpedia.org/sparql'

q = ('SELECT DISTINCT ?city WHERE {?city a <http://dbpedia.org/ontology/City> .} LIMIT 10')
result = sparql.query(dbpedia, q)

print(result.fetchone())

total= 0

for i in result:
    total +=1
    print ("row: ", i)

print ("total: ", total)

