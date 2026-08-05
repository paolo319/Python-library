"""age = int(input("Your age: "))

if age >=100:
    print("Too old")

elif age>=18:
    print("legal adult")

elif age < 0:
    print("Not yet born")

else:
    print("Not legal")

q = input("Are you eating? (Y/N): ")

if q == "Y":
    print("full")
else:
    print("Hungry")"""

name = str(input("Enter your name: "))
if name =="":
    print("Please enter your name")
else:
    print(f"Hello {name}!")

sale = True

if sale:
    print("Its for sale")
else:
    print("Not for sales")