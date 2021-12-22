n_eng = int(input())
eng = set(map(int,input().split()))
n_fre = int(input())
fre = set(map(int,input().split()))

roll = eng&fre
print(len(roll))
