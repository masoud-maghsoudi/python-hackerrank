import re
mobile_no_pattern = r"^[789]\d{9}$"
for line in range(int(input())):
    if re.match(mobile_no_pattern, input()):
        print("YES")
    else:
        print("NO")