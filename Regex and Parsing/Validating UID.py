import re

for _ in range(int(input())):
    s = input()
    flag = True
    #at least 2 Uppercase
    if len(re.findall(r"[A-Z]", s)) < 2:
        flag = False
    #at least 3 digit
    if len(re.findall(r"\d", s)) < 3:
        flag = False
    #only alphanumeric characters
    if re.search(r"[^A-Za-z0-9]+", s):
        flag = False
    #No Repetition & 10 character length
    if len(set(s)) != 10 or len(s) != 10:
        flag = False
    #Print the check result
    if flag :
        print("Valid")
    else:
        print("Invalid")