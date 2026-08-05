 #while loop = used to repeat a block of code as long as a
 #             condition remain 'True' we re-check the condition
 #             at the end of the loop

name = input("Enter your name: ")
while name == "":
    name = input("Please Enter your name: ")

age = int(input("Enter your age: "))
while age == 0 or age < 0:
    age = int(input("Age is not valid please retry again: "))

print(f'Hello {name}!')
print(f'Your age is {age}')

