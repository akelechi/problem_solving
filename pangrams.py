#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alpha_dict = {}
    theString = s.lower()
    theString = theString.replace(" ", "")
    for i in range(len(theString)):
        alpha_dict[theString[i]] = i

    number = len(alpha_dict.keys())
    if number == 26:
        return 'pangram'
    else:
        return 'not pangram'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
