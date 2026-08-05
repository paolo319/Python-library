import matplotlib.pyplot as plt
import numpy as np

#bar chart = Circular chart divided into slices to show percentages of the total.
#            Good for visualizing distribution among categories.

cat = ["Highschool", "Senior", "College", "Unemployed"]
val = np.array([300, 320, 400, 500])

#use this if you want to customize your own color pie
colors=["darkblue", "blue", "Green", "red"]

plt.pie(val, labels=cat, #this will display the pie and its category
            autopct="%1.1f%%",
            colors=colors,
            #creating a space cut of pie heres the sample
            explode=[0, 0, 0, 0.1],
            shadow=True,
            #to rotate you piechart heres how
            startangle=180)
plt.show()

