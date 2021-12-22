n = int(input())
inp = set(map(int,input().split()))
n_commmand = int(input())
sum = 0

for i in range(n_commmand):
    command = tuple(input().split())
    if command[0] == 'pop':
        inp.pop()
    elif command[0] == 'discard':
        inp.discard(int(command[1]))
    elif command[0] == 'remove':
        inp.remove(int(command[1]))

for i in inp:
    sum += i
print(sum)
