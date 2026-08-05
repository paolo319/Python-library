import matplotlib.pyplot as plt
import numpy as np

#Figure = The entire canvas 
#Ax = A single plot (subplot)
x = np.array([1, 2, 3, 4, 5])
                        #Rows/Column this create a many rows/columns
figure, axes = plt.subplots(2, 2)
#axes[0, 0].plot()
   #Rows/Column
axes[0, 0].plot(x, x*2, color="red")
axes[0, 0].set_title("x*2")#display the title
   #Rows/Column
axes[0, 1].bar(x, x**2, color="cyan")#this is just example about the bar
axes[0, 1].set_title("x**2")

   #Rows/Column
axes[1, 0].plot(x, x**3, color="blue")
axes[1, 0].set_title("x**3")

   #Rows/Column
axes[1, 1].plot(x, x**4, color="green")
axes[1, 1].set_title("x**4")

plt.tight_layout()#this prevent or fit in place
plt.show()