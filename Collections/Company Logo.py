from collections import Counter

if __name__ == '__main__':
    s = list(input())
    s.sort()
    top = 0
    counter = Counter(s)    
    result = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    for key, value in result.items():
        print(key, value, sep=' ')
        top += 1
        if top == 3: break