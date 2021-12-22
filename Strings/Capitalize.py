#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    str_out = ""
    for i in range(0,len(s)):
        if i == 0:
            str_out += s[i].upper()
        elif s[i-1].isspace():
            str_out += s[i].upper()   
        else:
            str_out += s[i]
    return str_out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
