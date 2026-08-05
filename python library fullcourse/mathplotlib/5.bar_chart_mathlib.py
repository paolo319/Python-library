import matplotlib.pyplot as plt
import numpy as np

#bar chart = compare categories of data by representing each category
#with a bar

cat = ["Grains", "Fruit", "Vegtables", "Protein", "Dairy", "Sweets"]
val = np.array([4, 3, 2, 5, 3, 1])

plt.bar(cat, val, color="green")#color or custumization is optional
#plt.barh(cat, val)#Good for rating a character as a example
plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()



