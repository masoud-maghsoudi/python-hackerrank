import re
for _ in range(int(input())):
    print(bool(re.search(r"^(\+|-)?\d*\.\d*.$", input())), sep='\n')