#for loop = used to iterate over a sequence(string, list, tuple, set)
#           or used to repeat a block of code an exact amount of times
"""
for i in range(10):
    #print(1)#it will print 1 only to 10
    print(i)#count 0 up to 9(total of 10)
    """
"""
          #first is inclusive the second is exclusive
for i2 in range(1, 11):#Now using this will start at 1 instead of index 0
    print(i2)#count 1 up to 10
    """

"""
     #You can use other number to see the example on the third value of paranthesis inside
for i3 in range(1, 11, 2):#Now it used the odd counting or skip after the count
    print(i3)
"""
"""
name = "Paolo E. Montalban"

for letter in name:
    print(letter)#it will print but single letter every single line
"""
"""
#used this instead if you want to stay in single line
name2 = "Paolo E. Montalban"

for letter in name2:
    #print(letter, end="")#end is used for space of the string
    #heres the example
    #print(letter, end="-")#it will dash(-) every single letter
    print(letter, end=" ")#it will space every single letter
"""

#Now lets add the time module(for the accurate print counting seconds)
import time
#Now lets set a bomb using reversed counting
for b in range(10, 0, -1):
    print(b)
    time.sleep(1)#used for count a specific purpose need
    #Now escaping the for loop
print("rest in peace my granny just hit by bazooka")