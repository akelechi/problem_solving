#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[0:2] == '12' and s[8]== 'A':
        return ('00'+ s[2:8])
    elif s[8] == 'A' or s[0:2]=='12':
        return s[0:8]
    else:
        first_stuff = int(s[0:2]) + 12
        first_stuff = str(first_stuff)
        s_list = list(s)
        for i in range(0, 2):
            s_list[i] = first_stuff[i]
            new_s = ''.join(s_list)
    return new_s[0:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
