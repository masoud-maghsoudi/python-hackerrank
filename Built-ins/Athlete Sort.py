if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    result = list(sorted(arr, key=lambda item: item[k]))
    for i in result:
        print(" ".join([str(j) for j in i]))