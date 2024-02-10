#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    counter = 0
    current_sum = 0
    if m == 1:
        for i in range(len(s)):
            if s[i] == d:
                counter+=1
        return counter
    else:
        for i in range(len(s)-m+1):
            for j in range(m):
                current_sum +=s[i+j]
            else:
                if current_sum == d:
                    counter+=1
                current_sum=0
        return counter
            
            
                
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
