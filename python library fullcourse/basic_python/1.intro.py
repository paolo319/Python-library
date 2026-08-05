#basic Variable use (str, int, float, boolean)

name = "me"
year = 2026
gwa = 1.5
student = True
print(f"My name is: {name}")
print(f"Year today is: {year}")
print(f"Grade is {gwa}")

if student:
    print("A Student")
else:
    print("not")

# the typecasting part see it what type of variable class of each example
print(type(name))
print(type(year))
print(type(gwa))
print(type(student))

#trying converting the float to int example
gwa = int(gwa)
#gwa += 1
print(gwa)

#another example converting to int to string note: if you try to convert a name str to
#number it will show error
#If you try to multiply a different variable such as str and int it will show error
year = str(year)
year += "1" #if you want to multiply using str the value should also be a string
print(year)
#sample for bool typescript
sample_name = "Me" #with name str will return true 
no_name = "" #without name str will return false
sample_name = bool(sample_name)
no_name = bool(no_name)
print(sample_name), print(no_name)
