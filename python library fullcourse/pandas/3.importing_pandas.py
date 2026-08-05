import pandas as pd

""" Excel Example"""
df = pd.read_csv("data.csv")
print(df)#it will print the data inside the csv 
#to show all the string use this
#print(df.to_string())#it will show all the data


df2 = pd.read_json("pokemon.json")
print(df2.to_string())
