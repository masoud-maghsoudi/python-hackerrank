import re

for line in range(int(input())):
    s = input()
    result = re.sub(r"(?<= )&& ", "and ", s)
    result = re.sub(r"(?<= )\|\| ", "or ", result)
    print(result)