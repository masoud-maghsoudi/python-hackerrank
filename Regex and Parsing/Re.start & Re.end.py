import re
S, k = input(), input()
match = re.finditer(r"(?=(%s))" % k, S)
flag = False
for m in match:
    flag = True
    print("({}, {})".format(m.start(), m.start()+len(k)-1))
if not flag:
    print("(-1, -1)")