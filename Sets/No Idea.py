inp = list(map(int, input().split()))
n, m = inp[0], inp[1]
check = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for i in check:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
    else:
        pass
print(happiness)
