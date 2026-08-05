unit = input("is this temperature is in celsius or fahrenheit(C/F):")
temp = float(input("Enter a temperature: "))

if unit == "C" or unit == "c":
    temp = ((9 * temp) / 5 + 32)
    print(f"The temperature of fahrenheit is {temp}~f")
elif unit == "F" or unit == "f":
    pass
else:
    print(f"Unit {unit} is an invalid measurement")