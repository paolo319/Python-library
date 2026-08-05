"""Logical operator = evaluate multiple conditions(or, and, not)
                      or = at least one conditon must be true
                      and = both condition must be true
                      not = invert conditions(not, false, not true)
"""

temp = 25
rain = False

if temp > 35 or temp < 0 or rain:
    print("Its raining")
else:
    print("Not raining")

name = "paolo"
pas = "12"

if name == "paolo" and pas == "123":
    print("Successful")
elif name == "paolo" and not pas =="123":
    print("wrong password")
else:
    print("Access denied")


