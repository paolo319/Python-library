import numpy as np
#Scalar arithmetic

"""
array = np.array([1, 2, 3])

print(array + 1)#it increase inside of array list
print(array - 2)#[-1  0  1]
print(array * 3)#times inside the array list
print(array / 4)#[0.25 0.5  0.75]
print(array ** 5)"""

#Vectorized math func

array = np.array([1, 2, 3])

print(np.sqrt(array))#[1.   1.41421356 1.73205081]

array_2 = np.array([1.01, 2.5, 3.99])
print(np.around(array_2))#[1. 2. 4.]
print(np.floor(array_2))#[1. 2. 3.]
print(np.ceil(array_2))#[2. 3. 4.]

#A build in Pi value
print(np.pi)#3.141592653589793

#Exercise
radii = np.array([1, 2, 3])
print(np.pi * radii ** 2)#[ 3.14159265 12.56637061 28.27433388]

#Element-wise arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(array1 + array2)#[5 7 9]It will increase each value
print(array1 - array2)#[-3 -3 -3]
print(array1 * array2)#[ 4 10 18]
print(array1 / array2)#[0.25 0.4  0.5 ]
print(array1 ** array2)#[  1  32 729]

#Comparison operator
score = np.array([91, 55, 100, 73, 82, 64])

#print(score == 100)#[False False  True False False False]

score[score < 60] = 0
print(score)#[ 91   0 100  73  82  64]