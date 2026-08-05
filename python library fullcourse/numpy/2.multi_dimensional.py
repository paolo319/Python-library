import numpy as np

#array = np.array("A")#This is 0 ndim example
#array = np.array(["A", "B", "C"])#This is one ndim example
"""
array = np.array([["A", "B", "C"],
                 ['D', 'E', 'F'],
                 ['H', 'I', 'J']])#This is two dimension array why?
                 #You see at the start of paranthesis we used 2 [
                 #Thats what i noticed
"""
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                 [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                 [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
                 #this is the 3rd dimension of array
                 #The reason why i add this - its because it will affect/detected because
                 #its a 3 dimension

#ndim means number of dimension
print(array.ndim)
print(array.shape)#think like a cake in layer
#Meaning of 3, 3 ,3 is elements inside
#first 3 is layers second is rows and the last is columns
#Note we used index not elements

#Now getting the specific layer, rows, and column

#print(array[0][0][0])#this is known as chain indexing
#but we have access to called multidimensional indexing
#is faster than chain indexing heres how

print(array[1, 1, 1])#Expected output will be N in guess

array2 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                 [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                 [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
            #A                    Y               B
word = array2[2, 0, 0] + array2[2, 2, 0] + array2[0, 0, 1] + array2[0, 0, 0] + array2[2, 0, 2]
#                                                                    A                   U
print(word)
