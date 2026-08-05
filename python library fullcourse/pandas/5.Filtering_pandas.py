import pandas as pd

df = pd.read_csv("data.csv")
#filtering = keeping the data rows that match a condition

height = df[df["Height"] > 2]
weight = df[df["Weight"] >100]
legend = df[df["Legendary"] == 1]#You can use bolean(True) it also equal to 1
water = df[df["Type1"] == "Water"]

#if you want to print the it dont have a type 1 but it have in the type 2 heres how
#We gonna use the C style operator |, & instead of or logical operator
#type_data = df[(df["Type1"] == "Water") |
#            (df["Type2"] == "Water")] 

ff = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(ff)