import matplotlib.pyplot as plt
#print(matplotlib.__version__)
import numpy as np

"""x = [2020, 2021, 2022, 2023, 2024]
y = [20, 30, 15, 10, 30]"""
x = np.array([2020, 2021, 2022, 2023, 2024])
y = np.array([20, 30, 15, 10, 30])

plt.plot(x, y)

plt.show()