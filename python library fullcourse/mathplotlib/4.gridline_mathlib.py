import matplotlib.pyplot as plt
import numpy as np

#grid() = help make plots easier to read by adding reference lines
x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.grid()
"""use this to make a custom grid line display here is the sample
plt.grid(axis="x")
plt.grid(axis="y, linewidth=2, color="gray", linestyle="solid")"""
plt.plot(x, y)
plt.show()