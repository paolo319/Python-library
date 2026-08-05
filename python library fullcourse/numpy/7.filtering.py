import numpy as np 
#Filtering = Refers to the process of selecting elements
#            from an array that match a given condition

"""
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                [39, 22, 15, 99, 18, 19, 20, 21]])

teenage = ages[ages < 18]
print(teenage)#17 16 15]

adult = ages[(ages >= 18) & (ages < 65)]
print(adult)#[21 19 20 30 18 39 22 18 19 20 21]

senior = ages[ages >= 65]
print(senior)#[65 99]

even = ages[ages % 2 == 0]
print(even)#[20 16 30 18 22 18 20]

odd = ages[ages % 2 != 0]
print(odd)#[21 17 19 65 39 15 99 19 21]

"""
#where function for preserve the data the original shape of data
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                [39, 22, 15, 99, 18, 19, 20, 21]])
adult = np.where(ages >= 18, ages, 0)
print(adult)#[[21  0 19 20  0 30 18 65]
            #[39 22  0 99 18 19 20 21]]