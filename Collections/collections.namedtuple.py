from collections import namedtuple

N = int(input().strip())
Student = namedtuple('Student', input().strip())
Sum = 0

for _ in range(N):
    col = input().split()
    student = Student(col[0],col[1],col[2],col[3])
    Sum += int(student.MARKS)
print('{:.2f}'.format(Sum/N))
