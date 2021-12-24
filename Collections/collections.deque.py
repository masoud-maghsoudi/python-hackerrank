from collections import deque
N = int(input())
deq = deque()
for i in range(N):
    cmd = list(input().split())
    if cmd[0] == 'append': deq.append(cmd[1])
    elif cmd[0] == 'appendleft': deq.appendleft(cmd[1])
    elif cmd[0] == 'pop': deq.pop()
    elif cmd[0] == 'popleft': deq.popleft()
for i in deq: print(i, end=' ')