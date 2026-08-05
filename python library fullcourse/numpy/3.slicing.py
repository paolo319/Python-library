import numpy as np

#we use the 2d array
#            index 0  1  2  3     columns
array = np.array([[1, 2, 3, 4], #index 0 or -4
                 [5, 6, 7, 8],  #index 1 or -3
                 [9, 10, 11, 12],  #index 2 or -2
                 [13, 14, 15, 16]]) #index 3 or -1
"""
#array[start:end:step]
#start index example
print(array[0])#This will return [1 2 3 4]
print(array[-1])#this will return [13, 14, 15, 16]
print()
#end index example
print(array[0:3])#It will display 1 to 12(not include the rest)
print(array[1:4])#5 to 16 not included the 1 - 4
print()
#step example
print(array[0:4:2])#this will display the first row and the third row
print(array[::4])#this will display all rows
print(array[::-1])#this will return all rows but in reverse
"""
#Now  we'll get into column selection
#selecting first rows and first index to print only
print(array[:, 0])#it will display [ 1  5  9 13]
print(array[:, 0:3])#it will print the first and third column in all rows 
#but skip to last column
print(array[0:2, 0:2])
print(array[0:2, 0])