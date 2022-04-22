from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("https://linkeddata.uriburner.com/sparql")
sparql.setQuery("""
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bd: <http://www.bigdata.com/rdf#>
PREFIX dct: <http://purl.org/dc/terms/>


SELECT DISTINCT
        ?dbpediaID
        (?item  as ?wikidataID)
        (xsd:string(?label) as ?name)
        ?description ?subjectText ?label
        ?image ?picture
WHERE {
          SERVICE <https://query.wikidata.org/sparql>
          {
              SELECT DISTINCT ?item ?numero (SAMPLE(?pic) AS ?picture)
              WHERE {
                        ?item p:P528 ?catalogStatement .
                        ?catalogStatement ps:P528 ?numero .
                        ?catalogStatement pq:P972 wd:Q14530 .
                        OPTIONAL {?item wdt:P18 ?pic } .

                        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
                    }
              GROUP BY ?item  ?numero ORDER BY ?numero
              }

          SERVICE <https://dbpedia.org/sparql>
          {
              SELECT ?dbpediaID ?label ?image ?description ?subjectText
              FROM <http://dbpedia.org>
                   WHERE { ?dbpediaID owl:sameAs ?item  ;
                                      rdfs:label ?label ;
                                      foaf:depiction ?image;
                                      rdfs:comment ?description ;
                                      dct:subject [ rdfs:label ?subjectText ] .
                           FILTER (LANG(?label) = "en")
                           FILTER (LANG(?description) = "en")
                         }
      }
}LIMIT 10""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result)
    #print(result["label"]["value"])