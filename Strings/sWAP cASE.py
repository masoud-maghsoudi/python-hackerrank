def swap_case(s):
    str_out = ""
    for char in s:
        if char.isupper():
            str_out += char.lower()
        elif char.islower():
            str_out += char.upper()
        else:
            str_out += char
    return str_out

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
