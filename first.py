import sparql

print("please work")

# q = ('SELECT DISTINCT ?station, ?orbits WHERE { '
#       '?station a <http://dbpedia.org/ontology/SpaceStation> . '
#       '?station <http://dbpedia.org/property/orbits> ?orbits . '
#       'FILTER(?orbits > 50000) } ORDER BY DESC(?orbits)')
# result = sparql.query('http://dbpedia.org/sparql', q)





# q = ('PREFIX wd: <http://www.wikidata.org/entity/>'
#         'PREFIX wds: <http://www.wikidata.org/entity/statement/>'
#         'PREFIX wdv: <http://www.wikidata.org/value/>'
#         'PREFIX wdt: <http://www.wikidata.org/prop/direct/>'
#         'PREFIX wikibase: <http://wikiba.se/ontology#>'
#         'PREFIX p: <http://www.wikidata.org/prop/>'
#         'PREFIX ps: <http://www.wikidata.org/prop/statement/>'
#         'PREFIX pq: <http://www.wikidata.org/prop/qualifier/>'
#         'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>'
#         'PREFIX bd: <http://www.bigdata.com/rdf#>)'
#         'SELECT ?s ?desc WHERE {'
#         '?s wdt:P279 wd:Q7725634 .'
#         'OPTIONAL {'
#             '?s rdfs:label ?desc filter (lang(?desc) = "en").'
#             '}'
#         '}'
#     )


# q = ('PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>'
#         'SELECT ?s ?s_label'
#         'WHERE{' 
#         '?s a <http://dbpedia.org/ontology/City>.'
#         '?s rdfs:label ?s_label .'
#         '} LIMIT 100)')


# q = ('SELECT distinct * WHERE {'
#         '?item wdt:P31/wdt:P279* wd:Q16917;'
#         'wdt:P625 ?geo .'
#         '} LIMIT 10)')
# q = ('%23Cats%0ASELECT%20%3Fitem%20%3FitemLabel%20%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20wdt%3AP31%20wd%3AQ146.%20%23%20Must%20be%20of%20a%20cat%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%20%23%20Helps%20get%20the%20label%20in%20your%20language%2C%20if%20not%2C%20then%20en%20language%0A%7D')

q = ('SELECT DISTINCT ?city WHERE {?city a <http://dbpedia.org/ontology/City> .} LIMIT 10')




# endpoint = 'https://query.wikidata.org/sparql?'
# s = sparql.Service(endpoint, "utf-8", "GET")
result = sparql.query('http://dbpedia.org/sparql', q)
# print(s)
# result = s.query(q)
print(result.variables)




# print (result)

# for row in result:
#     print ('row:', row)
#     values = sparql.unpack_row(row)
#     print (values[0], "-", values[1], "orbits")



