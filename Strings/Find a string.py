def count_substring(string, sub_string):
    result = 0
    for i in range(len(string)):
        if string[i]==sub_string[0]:
            j = i
            counter = 0
            for k in range(len(sub_string)):
                if j >= len(string):
                    break
                if string[j]==sub_string[k]:
                    counter += 1
                    j += 1
                else:
                    break
            if counter == len(sub_string):
                result += 1                                 
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
