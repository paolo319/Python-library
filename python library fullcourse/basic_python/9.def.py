#function = A block of reusable code
#           place () after the function name to invoke it
"""
def happy():
    print("Happy birthday to you")
    print("You are now old")
    print("Happy birthday to you")
    print()

happy()#You will execute the code above
happy()#This will repeat the code above 2 times

def greet(name, age):
    print("Hello", name)
    print(f'You are now {age} years old')
    print("Happy birthday to you again")
    print()

greet("Paolo", 21)

#execise 1

def display(name, year, course):
    print(f'Hello {name}')
    print(f'{year} Year College')
    print(f'Your course is {course}')

display("Paolo E. Montalban", "3rd", "Information Technology")
"""

#return = statement used to end of a function
#         and send a result back to the caller

def add (x, y):
    z = x + y
    return z

def min (x, y):
    z = x - y
    return z

def times (x, y):
    z = x * y
    return z

def divide (x, y):
    z = x / y
    return z

print(add(32, 35))#example call

#exercise 2
def create(first,mid, last):
    first = first.capitalize()
    mid = mid.capitalize()
    last = last.capitalize()
    return first + " " + mid + " " + last

fullname = create("Paolo", "E", "Montalban")
print(fullname)