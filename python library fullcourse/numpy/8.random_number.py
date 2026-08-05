import numpy as np 
"""
#rng = np.random.default_rng()#putting inside a "seed" will just give
                             #you a same result just like minecraft
                             #if you use same seed it will genrate the world the
                             #same result but if you dont put seed inside the paranthesis
                             #numpy will create for you
rng = np.random.default_rng(seed=1)#check the example in terminal
print(rng.integers(1, 7))#dice for example
#print(rng.integers(low=1, high=101))#low/high are optional for this
print(rng.integers(low=1, high=101, size=3))#lets say you genrate number 3 piece
print(rng.integers(low=1, high=101, size=(3, 2)))#now we have 2 dimensional
"""

"""
np.random.seed(seed=1)#this genrate the same result
print(np.random.uniform())
print(np.random.uniform(low=-1))
print(np.random.uniform(low=-1, high=1, size=3))
print(np.random.uniform(low=-1, high=1, size=(3, 2)))
"""

"""
rng = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)#it will shuffle the value inside
"""

rng = np.random.default_rng()
#fruits = np.array(["Apple", "Orange", "Banana", "Coconut", "Pineapple"])
#fruit = rng.choice(fruits)#now it shuffle but only display 1 randomly
#fruit = rng.choice(fruits, size=3)#now it shuffle but only display 3 randomly
fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])
fruit = rng.choice(fruits, size=(3, 3))#now it display 2d array
print(fruit)