import numpy as np
#Broadcasting allows Numpy to perform operations on arrays
#with different shapes by virtually expanding dimensions
#so they match the larger arrays shape

#The dimensions have the same size
#or
#One of the dimension has size of 1
"""
array1 = np.array([[1, 2, 3, 4],#this is the first example
     
                #[5, 6, 7, 8, 9, 10]])#if you do this will not compatible
                #because it doesnt match the row and colums
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])#Now it match
array2 = np.array([[1], [2], [3], [4]])
print(array1.shape)#(1, 4) # (4, 4) after we add 5-16
print(array2.shape)#(4, 1) #(4, 1) after we add 5-16

print(array1 * array2)
#[[ 1  2  3  4]
 #[ 2  4  6  8]
 #[ 3  6  9 12]
 #[ 4  8 12 16]]  this is the first example before adding 5-16
"""

#lets do a multiplication table
array_1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array_2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array_1.shape)#(1, 10)
print(array_2.shape)#(10, 1)
print(array_1 * array_2)
#heres the result
"""
[[  1   2   3   4   5   6   7   8   9  10]
 [  2   4   6   8  10  12  14  16  18  20]
 [  3   6   9  12  15  18  21  24  27  30]
 [  4   8  12  16  20  24  28  32  36  40]
 [  5  10  15  20  25  30  35  40  45  50]
 [  6  12  18  24  30  36  42  48  54  60]
 [  7  14  21  28  35  42  49  56  63  70]
 [  8  16  24  32  40  48  56  64  72  80]
 [  9  18  27  36  45  54  63  72  81  90]
 [ 10  20  30  40  50  60  70  80  90 100]]
"""