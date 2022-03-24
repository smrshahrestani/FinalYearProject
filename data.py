
titleList = []
queryList = []
predicateList = []
answerQueryList = []

# query 1
title1 = "Title 1"
query1 = """
    SELECT Q1
"""
predicate1 = ["predicate 1"]
answerQuery1 = """
    answer 1
"""
titleList.append(title1)
queryList.append(query1)
predicateList.append(predicate1)
answerQueryList.append(answerQuery1)

# query 2
title2 = "Title 2"
query2 = """
    Q2
"""
predicate2 = ["predicate 2"]
answerQuery2 = """
    answer 2
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


