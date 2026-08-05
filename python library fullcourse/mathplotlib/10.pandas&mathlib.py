import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

#print(df["Type1"].value_counts())
#type_count = df["Type1"].value_counts()
type_count = df["Type1"].value_counts(ascending=True)#now be in reverse order

plt.barh(type_count.index, type_count.values, color="green", edgecolor="black")

plt.title("Pokemon Primary Type")
plt.xlabel("Total")
plt.ylabel("Type")
plt.tight_layout()#Everything is fit
plt.show()
