#another sample for this is an basic input function

#input()#to type in the command prompt

name = input("what is your name?:")
print(f"Hello {name}!")

#trying variable int typescript sample
age = input("Your age increase times 2:")
age = int(age)
age += 2
print(age)
#use this instead for better input code for better prompt input
#age = int(input("Your age increase times 2"))

#exercise 1: rectangle area calculator note you can mix float and int because it the
#same number type not such str and bool only not valid if you enter float to the
#int variable

length = int(input("length: "))
width = float(input("width: "))
area = length * width
print(f"the area of rectangle is: {area}cm")

#Exercise 2: Shooping cart program
item = input("name of item: ")
price = float(input("Price of item: "))
q = int(input("how many would you like?: "))
total = price * q
print(f"You brought {q}x of {item}/s")
print(f"that would be {total} Pesos of {item}")