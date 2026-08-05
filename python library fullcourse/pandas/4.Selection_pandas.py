import pandas as pd

#df = pd.read_csv("data.csv")
#Selection By Column
#use .to_string() to show all the data
#print(df["Name"].to_string())#it will print all the data names only
#print(df["Height"])
#print(df["Weight"])
#for multiple Selection
#print(df[["Name", "Height", "Weight"]])

#Selection of Rows
#if you dont want to remember its number but name heres how
#print(df.loc[0])#It will only show only the specific data according to index

#if you to display only the specific rows heres how
#df = pd.read_csv("data.csv", index_col="Name")
#print(df)#Now it will display the name and the rest data without index and elements display

#to search for the name as example
#print(df.loc["Pikachu"])#It will display its data

#if you dont want all the data of one name and only specific heres how
#print(df.loc["Charizard", ["Height", "Weight"]])#It will display its data
#print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])#Start to end
#print(df.iloc[0:11])#also start to end
#print(df.iloc[0:11:2])#If you want every second row
#print(df.iloc[0:11:2, 0:3])#showing specific data only colums

#Exercise for searching
df = pd.read_csv("data.csv", index_col="Name")

pok = input("Enter a Pokemon name: ")
try:
    print(df.loc[pok])
except KeyError:
    print(f"{pok} not found")
