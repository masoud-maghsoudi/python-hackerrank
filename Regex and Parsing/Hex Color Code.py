import re

RGB_pattern = r'#[0-9A-Fa-f]{3,6}'
flag = False
for _ in range(int(input())):
    for string in input().split():
        if string == "{":
            flag = True
        elif string == "}":
            flag = False
        test = re.search(RGB_pattern, string)
        if test and flag:
            print(test[0])