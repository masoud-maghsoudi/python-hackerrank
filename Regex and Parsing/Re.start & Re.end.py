import re
S, k = input(), input()
for m in re.finditer(k, S):
    if m:
        print("({}, {})".format(m.start(), m.end()-1))
    else:
        print("-1, -1")