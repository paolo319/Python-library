#weight converter

weight = float(input("Put your weight: "))
unit = input("(Kg or pounds): ")

if unit == "kg":
    weight = weight / 2.205
    units = "kilograms"
    print(f"Your weight is {round(weight, 2)} {units}")
elif unit == "pounds":
    weight = weight * 2.205
    units = "pounds"
    print(f"Your weight is {round(weight, 2)} {units}")
else:
    print(f"{unit} is not valid input")

