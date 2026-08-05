import matplotlib.pyplot as plt
#print(matplotlib.__version__)
import numpy as np

"""x = [2020, 2021, 2022, 2023, 2024]
y = [20, 30, 15, 10, 30]"""
x = np.array([2020, 2021, 2022, 2023, 2024])
#y = np.array([20, 30, 15, 10, 30])
y1 = np.array([20, 30, 15, 10, 30])
y2 = np.array([5, 15, 9, 20, 25])
y3 = np.array([10, 40, 15, 21, 5])

#this is for y2
line_style = dict(marker="o",
                  markersize=20,
                  markerfacecolor="cyan",
                  markeredgecolor="red",
                  linestyle="dashed",
                  linewidth=4)
                 # color="darkblue")


plt.plot(x, y1, marker=".",  #you can use O, *, and . to see the example mark
               markersize=30,# You can use ms instead of markersize
               markerfacecolor="red",#you use mfc instead of markerfacecolor
               markeredgecolor="red",#mec
               #option below dotted, dashed, dashdot, none and solid
               linestyle="solid",
               linewidth=4,#adjusting the line width
               color="green")#changing color line
plt.plot(x, y2, ** line_style)
plt.plot(x, y3, color="blue", ** line_style)#you can pass the unique color inside of paranthesis
plt.show()