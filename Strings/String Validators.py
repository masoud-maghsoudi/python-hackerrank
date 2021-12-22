if __name__ == '__main__':
    s = input()
    flag = []

    for i in range(5):
        flag.append(False)
    for i in s:
        if not flag[0]:
            flag[0] = i.isalnum()
        if not flag[1]:
            flag[1] = i.isalpha()
        if not flag[2]:
            flag[2] = i.isdigit()
        if not flag[3]:
            flag[3] = i.islower()
        if not flag[4]:
            flag[4] = i.isupper()
    
    for i in range(5):
        print(flag[i])
