import textwrap

def wrap(string, max_width):
    string_len = len(string)
    output = ""
    for i in range(string_len):
        if i%max_width == max_width-1:
            output += string[i]+"\n"
        else:
            output += string[i]
    return output

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
