import math
"""
print(math.pi)
print(math.e)


x = 9
ceil = 9.1
floor = 9.9

result1 = math.sqrt(x)
result2 = math.ceil(ceil)
result3 = math.floor(floor)
print(result1, result2, result3)"""

#exersise 1
radius = float(input(f"Enter a radius of circle: "))
cirumferences = 2 * math.pi * radius
print(f"the circumferences is {cirumferences}cm")
print(f"the circumferences convert to round is: {round(cirumferences, 2)}cm")
#depend on what digit you want to put but i put to decimal of remain digit
#exersise 2
area = math.pi * pow(radius, 2)
print(f"The area of circle is: {area}cm")
print(f"The area of circle is: {round(area, 1)}cm")

#Exersie 3

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
#c = pow(a, 2) + pow(b, 2)
c = math.sqrt(pow(a, 2) + pow(b, 2))
print("Side C= ", c)