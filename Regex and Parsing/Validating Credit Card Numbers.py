import re

for _ in range(int(input())):
    s = input()
    card = ""
    flag = True
    #seperation with - and stripping seperators
    if "-" in s:
        if not re.match(r"\d{4}-\d{4}-\d{4}-\d{4}", s):
            flag = False
        for char in s:
            if char != "-":
                card += char
    else:
        card = s
    #start with 4,5,6
    if re.match(r"[^4-6]", card):
        flag = False
    #consist of digits and -
    if re.search(r"[^\d]", card):
        flag = False
    #not having 4 or more consecutive repeated digits
    if (re.search(r"(.)\1{3,}", card)):
        flag = False
    #16 digit legth check
    if len(card) != 16:
        flag = False
    #Print the check result
    if flag :
        print("Valid")
    else:
        print("Invalid")