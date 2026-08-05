import pandas as pd

""" Data Cleaning = the process of fixing/removing:
                    incomplete, incorrect or irrelevant data.
                    ~75% of work done with pandas is data cleaning"""


df = pd.read_csv("data.csv")

#1.Drop irrelevant columns
#df = df.drop(columns=["Legendary", "No"])#it will not display the specific column

#2.handle missing data. dropna = Drop not available/ fillna = fill the not available
#df = df.dropna(subset=["Type2"])#it drop only the column N/A data 
#df = df.fillna({"Type2": "none"})#It replace the value the NA to none

#3.fix inconsistent values
#df["Type1"] = df["Type1"].replace({"Grass" : "GRASS"})#It replace the data 
#If you want multiple changes
"""df["Type1"] = df["Type1"].replace({"Grass" : "GRASS",
                                   "Fire": "FIRE",
                                    "Water": "WATER"})
"""

#4. Standardize text
#df["Name"] = df["Name"].str.lower()#all the name will be small letter

#5. Fix data types
df["Legendary"] = df["Legendary"].astype(bool)#instead of returning of 1 or zero it 
#will return true or false instead

#6. Remove duplicate values
df = df.drop_duplicates()#It remove the duplicate data to display
print(df)