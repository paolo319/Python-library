import pandas as pd

"""Let use the calories tracking as a example """

#i used the dictionary
calories = {"day 1" : 1200, "day 2": 1500, "day 3": 1700}
cal = pd.Series(calories)

print("Calories per day")
print(cal)


print("You cheat at day 2:")
cal.loc["day 2"] += 500
print(cal)

#now lets say you didnt/did follow the amount calories most heres how
print("You didnt meet the calories requirements amount at")
print(cal[cal>=2000])
print("You meet the calories requirement at")
print(cal[cal<2000])