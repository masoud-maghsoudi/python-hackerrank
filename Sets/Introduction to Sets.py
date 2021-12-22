def average(array):
    sum = 0
    distinct_array = set(array)    
    for i in distinct_array:
        sum += i
    return('{:.3f}'.format(sum/(len(distinct_array))))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
