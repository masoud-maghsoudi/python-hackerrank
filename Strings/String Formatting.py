def print_formatted(number):
    pad = len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(pad," "),str(oct(i))[2:].rjust(pad," "),str(hex(i))[2:].upper().rjust(pad," "),str(bin(i))[2:].rjust(pad," "),sep=' ')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
