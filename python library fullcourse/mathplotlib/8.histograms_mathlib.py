import matplotlib.pyplot as plt
import numpy as np

#Histograms = A visual representation of the distribution of the
#             quantitative data. They group values into bins (intervals)
#             and counts how many fail in each range.

score = np.random.normal(loc=80, scale=10, size=100)
score = np.clip(score, 0, 100)

plt.hist(score, bins=10, edgecolor="black")

plt.title("Exam Scores")
plt.xlabel("SCores")
plt.ylabel("Number of students")
plt.show()