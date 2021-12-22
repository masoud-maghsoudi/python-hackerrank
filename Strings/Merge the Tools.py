def merge_the_tools(string, k): 
    for i in range(0,len(string),k):
        tmp = string[i:i+k]
        result = ''
        for char in tmp:
            if char not in result:
                result += char
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
