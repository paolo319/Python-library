import pandas as ex

#aggregate function = Reduces a set of value into a single summary value
#                    Used to summarize and analyze data
#                    Often used the groupby() function

df = ex.read_csv("data.csv")

#It apply Whole dataframe
#print(df.mean(numeric_only=True))#Average display
#print(df.sum(numeric_only=True))#Summary
#print(df.min(numeric_only=True))#Minimum
#print(df.max(numeric_only=True))#Maximum
#print(df.count())#Total of data each

#Single column
#print(df["Height"].mean())
#print(df["Height"].sum())
#print(df["Height"].min())
#print(df["Height"].max())
#print(df["Height"].count())

#now lets add the group function
group = df.groupby("Type1")
#print(group["Height"].mean())
#print(group["Height"].sum())
#print(group["Height"].min())
#print(group["Height"].max())
print(group["Height"].count())