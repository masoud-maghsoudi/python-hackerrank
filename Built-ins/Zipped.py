N, X = map(int, input().split())
scores = []
for i in range(X): scores.append(list(map(float, input().split())))
for i in zip(*scores):
    sum = 0
    for j in i:
        sum += j
    print(sum/X)