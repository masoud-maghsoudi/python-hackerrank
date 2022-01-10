import re

email_pattern = r"^<[A-Za-z](\w|-|\.)+@[A-Za-z]+\.[A-Za-z]{1,3}>$"
for _ in range(int(input())):
    name, email = list(input().split())
    if re.match(email_pattern, email):
        print("{} {}".format(name, email))