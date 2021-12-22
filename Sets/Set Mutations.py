n_S = int(input())
S = set(map(int,input().split()))
n_oper = int(input())

for i in range(n_oper):
    cmd = tuple(input().split())
    arg = set(map(int,input().split()))
    if cmd[0] == 'intersection_update':
        S.intersection_update(arg)
    elif cmd[0] == 'update':
        S.update(arg)
    elif cmd[0] == 'symmetric_difference_update':
        S.symmetric_difference_update(arg)
    elif cmd[0] == 'difference_update':
        S.difference_update(arg)
sum = 0
result = list(S)
for k in range(len(result)):
    sum += result[k]
print(sum)
