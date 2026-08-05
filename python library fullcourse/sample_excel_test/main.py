import pandas as pd

df = pd.read_csv("data_excel.csv", index_col="Id_no")

pok = input("Enter a name: ")
try:
    print(df.loc[pok])
except KeyError:
    print(f"{pok} not found")
