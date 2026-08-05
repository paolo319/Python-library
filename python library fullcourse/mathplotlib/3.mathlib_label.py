import matplotlib.pyplot as plt
import numpy as np
#x = np.array([2020, 2021, 2022, 2023])
#x = np.array(["8am-9am", "9am-10am", "10am-11am", "1pm-2pm"])
x = ["8am-9am", "9am-10am", "10am-11am", "1pm-2pm"]
y1 = np.array([20, 30, 15, 10])
y2 = np.array([5, 15, 9, 20])
y3 = np.array([10, 40, 15, 25])

plt.title("Library visit", fontsize=20,
                            family="arial",
                            fontweight="bold",
                            color="red") 
plt.xlabel("Year", fontsize=15,
                   family="arial",
                   fontweight="bold",
                   color="red")

plt.ylabel("students", fontsize=15,
                   family="arial",
                   fontweight="bold",
                   color="red")#colors not color

plt.tick_params(axis="both",
                colors="darkgreen")

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

#use this if you using a number to drop decimal display
#plt.xsticks(x)

plt.show()