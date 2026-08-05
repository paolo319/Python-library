# python Calculator

num1 = float(input("Enter your first Number: "))
ope = input("Select operator: +, -, *, /")
num2 = float(input("Enter Your second number: "))

if ope == "+":
    result = num1 + num2
    print(f"{num1} {ope} {num2} = {result}")
elif ope == "-":
    result = num1 - num2
    print(f"{num1} {ope} {num2} = {result}")
elif ope == "*":
    result = num1 * num2
    print(f"{num1} {ope} {num2} = {result}")
elif ope == "/":
    result = num1 / num2
    print(f"{num1} {ope} {num2} = {result}")
else:
    print("Not valid operator")