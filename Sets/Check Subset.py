testcase_no = int(input())
for i in range(testcase_no):
    elem_no = int(input())
    A = set(map(int,input().split()))
    elem_no = int(input())
    B = set(map(int,input().split()))
    print((A&B)==A)
