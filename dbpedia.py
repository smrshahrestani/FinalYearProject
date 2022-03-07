# NOT COMPATABLE WITH PYTHON 3

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





print "----"

for row in result:

    values = sparql.fetchall()
    print values[0], "-", values[1], "orbits"

print sparql.parse_n3_term(result)

print sparql.unpack_row(result, convert=None, convert_type={})