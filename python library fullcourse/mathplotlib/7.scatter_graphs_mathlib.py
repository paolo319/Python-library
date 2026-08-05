import matplotlib.pyplot as plt
import numpy as np

#scatter graph = Shows the relationship between two variable
#                Helps to identify a correlation (+, -, none)
#                Example: Study hours vs test scores

x = np.array([0, 1, 1, 3, 2])#Hours of study
y = np.array([70, 75, 90, 84, 88])#Grades Score

x2 = np.array([0, 2, 2, 1, 5])#Hours of study
y2 = np.array([77, 82, 79, 84, 95])#Grades Score

plt.scatter(x, y, color="skyblue", alpha= 0.5, s=200, label="Boys")

plt.scatter(x2, y2, color="red", alpha= 0.5, s=200, label="Girls")

plt.title("Students Habit")
plt.xlabel("Hours of study")
plt.ylabel("Grades")

plt.legend()#it display in the left side of the y axis
plt.show()