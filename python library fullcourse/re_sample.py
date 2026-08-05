# import re 

# def validate_phone(): 
#     print(">Welcome to the phone number validation") 
#     print("Type Enter to continue validate user country and phone number, if not Type Exit to end phone number validation") 
    
#     while True: 
#         print() 
#         option = input("=>Enter/Exit: ") 
        
#         if option == "enter" or option == "Enter" or option == "ENTER": 
#             print("Please choose the available country to validate user phone number") 
#             print("1.Philipine(+63)") 
#             print("2.Singapore(+65)") 
#             print("3.Nigeria(+234)") 
#             print("4.Australia(+61)") 
#             print("5.Canada(+1)") 
            
#             country = input("Select only 1/2/3/4/5: ") 
            
#             if country == "1": 
#                 print("Philipine(+63)") 
#                 number = input("09XXXXXXXXX: ") 
#                 digit = re.compile(r"^0[9]\d{9}$") 
#                 if digit.match(number): 
#                     print(number, "VALID Country Phone Number ✓") 
#                 else: 
#                     print(number, "INVALID Country Phone number X") 
#             elif country == "2": 
#                 print("Singapore(+65)") 
#                 number = input("XXXXXXXX: ") 
#                 digit = re.compile(r"^[8-9]\d{7}$") 
#                 if digit.match(number): 
#                     print(number, "VALID Country Phone number ✓") 
#                 else: 
#                     print(number, "INVALID Country Phone Number X") 
#             elif country == "3": 
#                 print("Nigeria(+234)") 
#                 number = input("0XXXXXXXXXX: ") 
#                 digit = re.compile(r"^0[7-9]\d{8}$") 
#                 if digit.match(number): 
#                     print(number, "VALID Country Phone Number ✓") 
#                 else: 
#                     print(number, "INVALID Country Phone Number X") 
#             elif country == "4": 
#                 print("Australia(+61)") 
#                 number = input("04XXXXXXXX: ") 
#                 digit = re.compile(r"^0[4]\d{8}$") 
#                 if digit.match(number): 
#                     print(number, "VALID Country Phone Number ✓") 
#                 else: 
#                     print(number, "INVALID Country Phone Number X") 
#             elif country == "5": 
#                 print("Canada(+1)") 
#                 number = input("1XXXXXXXXXX: ") 
#                 digit = re.compile(r"^1[2-9]\d{9}$") 
#                 if digit.match(number): 
#                     print(number, "VALID Country Phone Number ✓") 
#                 else: 
#                     print(number, "INVALID Country Phone Number X") 
#             else: 
#                 print("N/A Country Please Choose 1/2/3/4/5 Country selection only") 
                
#         elif option == "Exit" or option == "exit" or option == "EXIT": 
#             print("Time out") 
#             break 
#         else: 
#             print("try again")

# validate_phone()

# import re
# #text = '04-2425-031730'
# text = input("id:")
# pattern = re.compile(r'^\d{2}[-\s]\d{4}[-\s]\d{6}$')

# mat = re.findall(pattern, text)
# if mat:
#     print("success")
# else:
#     print("Unsuccess")

import re
import pandas as pd
pattern = re.compile(r'^\d{2}[-\s]\d{4}[-\s]\d{6}$')
#excel = pd.read_excel("Excel_sample_test.xlsx")
excel = pd.read_excel("Bachelor Of Science Information Technology.xlsx")

while True:
    text = input("enter id:").strip()
    #select = excel["Id_no"].astype(str).tolist()
    select = excel["Id"].astype(str).tolist()
    if pattern.match(text):
        if text in select:
            print("Connected")
        else:
            print("Correct but not found")

    else:
        print("Invalid")
