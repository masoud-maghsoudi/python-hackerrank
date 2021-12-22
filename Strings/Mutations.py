def mutate_string(string, position, character):
    lstring = list(string)
    lstring[position] = character
    output = "".join(lstring)
    return output

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
