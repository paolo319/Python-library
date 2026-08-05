import pandas as pd

#Dataframes = A tabular data structure with rows AND columns. 
# (2 Dimensional) Similar to an Excel spreadsheet

data = {"name": ["Steve fox", " Marduk Craig", "Armor King"],
        "age": [22, 40, 30]
}

#df = pd.DataFrame(data)
#print(df)
df = pd.DataFrame(data, index=["1", "2", "3"])
print(df.loc["1"])#it return steve fox
print(df.iloc[1]);#it return to Marduk Craig

#add new column
df["Hobby"] = ["Boxing", "Fame", "Revenge"]
#add new row
new_row = pd.DataFrame([{"name": "King", "age": 30, "Hobby": "Wrestling"}],
#adding new as row(optional)
#{"name": "King", "age": 30, "Hobby": "Wrestling"}],
#adding new index
index=["4", "5"])
df = pd.concat([df, new_row])
print(df)


