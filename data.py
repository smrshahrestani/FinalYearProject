# @Author: Seyed Mohammad Reza Shahrestani
# @date: 22/04/2022


# A Stupid Database

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
title3 = "Winner of the Academy Awards"
query3 = """
#Winner of the Academy Awards by Award and Time
SELECT DISTINCT ?item ?itemLabel ?time
{
    ?item wdt:P106/wdt:P279* wd:Q3455803 ; # Items with the Occupation(P106) of Director(Q3455803) or a subclass(P279)
          p:P166 ?awardStat .              # ... with an awarded(P166) statement
    ?awardStat pq:P805 ?award ;            # Get the award (which is "subject of" XXth Academy Awards)
               ps:P166 wd:Q103360 .        # ... that has the value Academy Award for Best Director(Q103360)
    ?award wdt:P585 ?time .                # the "point of time" of the Academy Award
    SERVICE wikibase:label {               # ... include the labels
        bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en"
    }
}
ORDER BY DESC(?time)
LIMIT 10
"""
predicate3 = ["$ is the winner of the", "$ has won the ", "The winner of the Academy Awards was $ in year ",]
answerQuery3 = """
#Winner of the Academy Awards by Award and Time
SELECT DISTINCT ?item ?awardLabel ?time
{
    ?item wdt:P106/wdt:P279* wd:Q3455803 ; # Items with the Occupation(P106) of Director(Q3455803) or a subclass(P279)
          p:P166 ?awardStat .              # ... with an awarded(P166) statement
    ?awardStat pq:P805 ?award ;            # Get the award (which is "subject of" XXth Academy Awards)
               ps:P166 wd:Q103360 .        # ... that has the value Academy Award for Best Director(Q103360)
    ?award wdt:P585 ?time .                # the "point of time" of the Academy Award
    SERVICE wikibase:label {               # ... include the labels
        bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en"
    }
}
ORDER BY DESC(?time)
LIMIT 10
"""
titleList.append(title3)
queryList.append(query3)
predicateList.append(predicate3)
answerQueryList.append(answerQuery3)

# query 4
title4 = "Winner of the Academy Awards - 2"
query4 = """
#Winner of the Academy Awards by Award and Time
SELECT DISTINCT ?item ?awardLabel ?time
{
    ?item wdt:P106/wdt:P279* wd:Q3455803 ; # Items with the Occupation(P106) of Director(Q3455803) or a subclass(P279)
          p:P166 ?awardStat .              # ... with an awarded(P166) statement
    ?awardStat pq:P805 ?award ;            # Get the award (which is "subject of" XXth Academy Awards)
               ps:P166 wd:Q103360 .        # ... that has the value Academy Award for Best Director(Q103360)
    ?award wdt:P585 ?time .                # the "point of time" of the Academy Award
    SERVICE wikibase:label {               # ... include the labels
        bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en"
    }
}
ORDER BY DESC(?time)
LIMIT 10
"""
predicate4 = ["the winner of $ is ", "$ was won by "]
answerQuery4 = """
#Winner of the Academy Awards by Award and Time
SELECT DISTINCT ?item ?itemLabel ?time
{
    ?item wdt:P106/wdt:P279* wd:Q3455803 ; # Items with the Occupation(P106) of Director(Q3455803) or a subclass(P279)
          p:P166 ?awardStat .              # ... with an awarded(P166) statement
    ?awardStat pq:P805 ?award ;            # Get the award (which is "subject of" XXth Academy Awards)
               ps:P166 wd:Q103360 .        # ... that has the value Academy Award for Best Director(Q103360)
    ?award wdt:P585 ?time .                # the "point of time" of the Academy Award
    SERVICE wikibase:label {               # ... include the labels
        bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en"
    }
}
ORDER BY DESC(?time)
LIMIT 10
"""
titleList.append(title4)
queryList.append(query4)
predicateList.append(predicate4)
answerQueryList.append(answerQuery4)


# query 5
title5 = "Winners of the Nobel Prize"
query5 = """
#People that received both Academy Award and Nobel Prize
SELECT DISTINCT ?Person ?NobelPrizeLabel WHERE {
  ?NobelPrize wdt:P279?/wdt:P31? wd:Q7191 .    # <- subtypes of nobel prize
  ?Person wdt:P166? ?NobelPrize .              # <- people awarded a nobel prize
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" .
  }
}ORDER BY DESC(?Person)
LIMIT 10
"""
predicate5 = ["the winner of $ is ", "$ is a valuable prize that was won by "]
answerQuery5 = """


#People that received both Academy Award and Nobel Prize
SELECT DISTINCT ?Person ?PersonLabel WHERE {
  ?NobelPrize wdt:P279?/wdt:P31? wd:Q7191 .    # <- subtypes of nobel prize
  ?Person wdt:P166? ?NobelPrize .              # <- people awarded a nobel prize
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" .
  }
}ORDER BY DESC(?Person)
LIMIT 10
"""
titleList.append(title5)
queryList.append(query5)
predicateList.append(predicate5)
answerQueryList.append(answerQuery5)


# query 6
title6 = "Winners of the Nobel Prize - 2"
query6 = """
#People that received both Academy Award and Nobel Prize
SELECT DISTINCT ?Person ?PersonLabel WHERE {
  ?NobelPrize wdt:P279?/wdt:P31? wd:Q7191 .    # <- subtypes of nobel prize
  ?Person wdt:P166? ?NobelPrize .              # <- people awarded a nobel prize
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" .
  }
}ORDER BY DESC(?Person)
LIMIT 10
"""
predicate6 = ["$ is the winner of ", "$ is the winner of Nobel prize in "]
answerQuery6 = """
#People that received both Academy Award and Nobel Prize
SELECT DISTINCT ?Person ?NobelPrizeLabel WHERE {
  ?NobelPrize wdt:P279?/wdt:P31? wd:Q7191 .    # <- subtypes of nobel prize
  ?Person wdt:P166? ?NobelPrize .              # <- people awarded a nobel prize
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" .
  }
}ORDER BY DESC(?Person)
LIMIT 10
"""
titleList.append(title6)
queryList.append(query6)
predicateList.append(predicate6)
answerQueryList.append(answerQuery6)


# A getter function to get the data from this file
# @return: [String: titles], [String: queries], [[String: predicate 1], [String: predicate 2], ...], [String: answer query]
def getData():
    return titleList, queryList, predicateList, answerQueryList