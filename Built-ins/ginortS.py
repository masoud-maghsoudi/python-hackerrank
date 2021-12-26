s = list(input())
result = dict(lower=[], upper=[], odd=[], even=[])
output = []
for i in s:
    if i.islower(): result['lower'] += i
    elif i.isupper(): result['upper'] += i 
    elif int(i)%2 == 1: result['odd'] += i
    else: result['even'] += i
for i in result.values(): 
    i.sort()
    output.extend(i)
print("".join(output))