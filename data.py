
titleList = []
queryList = []
predicateList = []
answerQueryList = []

# query 1
title1 = "Capital Cities"
query1 = """
# defaultView:BubbleChart
SELECT DISTINCT ?countryLabel ?population
{
  ?country wdt:P31 wd:Q6256 ;
           wdt:P1082 ?population .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
GROUP BY ?population ?countryLabel
ORDER BY DESC(?population)
LIMIT 10
"""
predicate1 = ["The Capital city of $ is ", "pred1 -2"]
answerQuery1 = """
    answer 1
"""
titleList.append(title1)
queryList.append(query1)
predicateList.append(predicate1)
answerQueryList.append(answerQuery1)

# query 2
title2 = "The Capital Cities"
query2 = """
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
predicate2 = ["The Capital City of $ is ", "The most important city of $ is "]
answerQuery2 = """
PREFIX bd: <http://www.bigdata.com/rdf#> 
PREFIX wd: <http://www.wikidata.org/entity/> 
PREFIX wdt: <http://www.wikidata.org/prop/direct/> 
PREFIX wikibase: <http://wikiba.se/ontology#> 
#added before 2016-10
SELECT DISTINCT ?country ?capital ?capitalLabel
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
titleList.append(title2)
queryList.append(query2)
predicateList.append(predicate2)
answerQueryList.append(answerQuery2)

# query 3
title3 = "Title 3"
query3 = """
    Q3
"""
predicate3 = ["predicate 3"]
answerQuery3 = """
    answer 3
"""
titleList.append(title3)
queryList.append(query3)
predicateList.append(predicate3)
answerQueryList.append(answerQuery3)

# query 4
title4 = "Title 4"
query4 = """
    SELECT Q4
"""
predicate4 = ["predicate 4"]
answerQuery4 = """
    answer 4
"""
titleList.append(title4)
queryList.append(query4)
predicateList.append(predicate4)
answerQueryList.append(answerQuery4)


print(queryList)
print(predicateList)

def getData():
    return titleList, queryList, predicateList, answerQueryList


