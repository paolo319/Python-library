"""
List [] = mutable, most flexible
tupple () + immutable, faster 
set {} = mutable (add/remove), unordered, No duplicate,
         Best for membership testing
"""
#example used of List[]

fruits = ["Apple", "Orange", "Banana", "Coconut"]
"""
print(fruits)#Output: ['Apple', 'Orange', 'Banana', 'Coconut']
print(fruit[0])#Output: Apple
"""
#You can you for loop to print each fruit
"""
#you can change the element value just like this
fruits[0] = "Pineapple"
#You can add new fruit element like this
fruits.append("Guava")
#You can remove elements like this
fruits.remove("Guava")#Now Guava will not include the print
#You can remove the element at a given index like this
fruits.pop(0)#The first element will now not include in print
#If you want to clear the list heres how
fruits.clear()#Now the entire list is remove
"""
"""
for fruit in fruits:
    #print(fruit)
    #used end instead to print in single line
    print(fruit, end=" ")
"""
"""
#set example since tupple is immutable
#because set has add/remove like append/remove, pop or clear idk
#You will noticed that position changes each time
fruits_2 = {"Apple", "Orange", "Banana", "Coconut"}
#You can add new fruit like this
fruits_2.add("Mango")
#You can remove fruit like this
fruits_2.remove("Mango")#Now this will not included

for fruit_2 in fruits_2:
    print(fruit_2, end=" ")

#You can use this as seachable like this
if "Apple" in fruits_2:
    print("Apple was found")
else:
    print("Fruit not found")
"""

#Exercise Searching name member
member = {"Paolo", "Rutz", "Jeriel"}
search = input("Enter name to search: ")

while True:
    if search in member:
        print(f"{search} was found")
        search = input("Enter name to search: ")
    else:
        print(f"{search} was not found")
        search = input("Enter name to search: ")
