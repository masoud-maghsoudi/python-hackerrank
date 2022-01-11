import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(list(matrix_item))

string = ''    
for i in range(m):
    for j in range(n):
        string += matrix[j][i]
result = re.sub(r"([a-zA-Z0-9]+)([\s!@#$%&]+)([a-zA-Z0-9])", r"\1 \3", string)
print(result)