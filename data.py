
queryList = []
predicateList = []

# query 1
query1 = """
    SELECT Q1
"""
predicate1 = "predicate 1"
queryList.append(query1)
predicateList.append(predicate1)

# query 2
query2 = """
    Q2
"""
predicate2 = "predicate 2"
queryList.append(query2)
predicateList.append(predicate2)

# query 3
query3 = """
    Q3
"""
predicate3 = "predicate 3"
queryList.append(query3)
predicateList.append(predicate3)

# query 4
query4 = """
    SELECT Q4
"""
predicate4 = "predicate 4"
queryList.append(query4)
predicateList.append(predicate4)



print(queryList)
print(predicateList)

def getData():
    return queryList, predicateList


