import re
m = re.search(r'([0-9|a-z|A-Z])\1+', input())
print(m.group(1) if m else -1)