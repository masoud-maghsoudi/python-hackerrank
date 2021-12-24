from collections import deque

T = int(input())
for i in range(T):
    size = int(input())
    block = deque(map(int, input().split()))
    last = pow(2,31)
    for j in range(size):
        if last >= block[0] and last >= block[-1]:
            if block[0]>block[-1]:
                last = block.popleft()
            elif block[-1]>block[0]:
                last = block.pop()
            elif block[0]==block[-1]:
                last = block.pop()
        else:
            print("No")
            break
        if len(block)==0:
            print("Yes")
            break