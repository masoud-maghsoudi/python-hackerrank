def wrapper(f):
    def fun(l):
        num = []
        for i in l:
            num.append("+91 {} {}".format(i[-10:-5], i[-5:]))
        num.sort()
        for i in num:
            print(i)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)