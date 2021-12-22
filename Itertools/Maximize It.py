import itertools

tests,mod = map(int, input().split())
maximum = 0
allLists = []

for t in range(tests):
  data = list(map(int, input().split()))
  data.pop(0)
  data = list(map(lambda x: x*x, data))
  allLists.append(data)

  
for each in itertools.product(*allLists):
  num = sum(each) % mod
  if num > maximum:
    maximum = num
  
print(maximum)