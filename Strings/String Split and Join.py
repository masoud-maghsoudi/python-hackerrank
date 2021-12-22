def split_and_join(line):
    tmp = line.split()
    return "-".join(tmp)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
