import string
def print_rangoli(size):
    
    alphabet=list(string.ascii_lowercase)
    for i in range(-size+1,size,1):
        rwords = alphabet[abs(i)+1:size]
        cwords = list(alphabet[abs(i)])
        lwords = rwords[::-1]
        words = lwords+cwords+rwords
        print('-'.join(words).center(4*size-3,'-'))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
