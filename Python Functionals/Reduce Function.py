from fractions import Fraction
from functools import reduce

<<<<<<< HEAD
def product(fracs):
    pass
#    t = # complete this line with a reduce statement
#    return t.numerator, t.denominator
=======

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)
    return t.numerator, t.denominator

>>>>>>> adee6dd232ad570d833d79f0d3cc7dc865ae396b

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)