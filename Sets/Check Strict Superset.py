A = set(map(int,input().split()))
sets_no = int(input())
flag = True
for i in range(sets_no):
    test = set(map(int,input().split()))
    if not ((len(A)>len(test)) and ((A&test)==test)):
        flag = False
        print(flag)
        break
if flag: print(flag)
