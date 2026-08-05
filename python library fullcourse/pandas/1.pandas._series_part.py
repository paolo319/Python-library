import pandas as pd

#print(pd.__version__) #show you the current version of pandas


"""pandas = A Pandas 1-Dimensional labeled array that can hold any
data type think of it like a single column in a spreedsheet (1-Dimensional)"""

# Integer / Float Examples
data = [100.1, 102.1, 104] 
series = pd.Series(data)
print(series)

#Strings Examples
datastring = ["A", "B", "C"]
string = pd.Series(datastring)
print(string)

#Bolean Examples
databol = [True, False, False]
bol = pd.Series(databol)
print(bol)

"""To make your own index custom heres how"""

ind = ["Paolo", "Rutz", "Justine"]
dex = pd.Series(ind, index=["04-2425,031730","04-2425-XXXXXX", "04-2425-XXXXXX"])
print(dex)

"""To return a value like the specific search of id heres how"""

ind2 = ["Paolo", "Rutz", "Justine"]
dex2 = pd.Series(ind2, index=["04-2425,031730","04-2425-XXXXXb", "04-2425-XXXXXc"])
print(dex.loc["04-2425,031730"])

"""To access the lock property or changing the value properties here how"""
ex = [1, 2, 3]
change = pd.Series(ex, index=["a", "b", "c"])
change.loc["a"] = 200
print(change)

"""Targeting data using index heres how"""
tar = ["Paolo", "Rutz", "Justine"]
get = pd.Series(ind, index=["04-2425,031730","04-2425-XXXXXX", "04-2425-XXXXXX"])
print(get.iloc[2])

"""Using a value meet number and return true or false heres how"""
number= [100, 102, 200, 500, 10]
num = pd.Series(number, index=["a", "b", "c", "d", "e"])
# use other like >=, <=, ==, or != for examples
print(num >=200)

"""Another example that meet the condition value heres how"""
number2= [100, 102, 200, 500, 10]
num2 = pd.Series(number2, index=["a", "b", "c", "d", "e"])
# use other like >=, <=, ==, or != for examples
print(num2[num2!=200])

