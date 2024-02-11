#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    ar = sorted(ar)
    current = ar[0]
    counter = 0
    numPairs = 0
    for i in range(n):
        if ar[i]== current:
            counter+= 1
            if i == n-1:
                numPairs += int(counter/2)
        else:
            current = ar[i]
            numPairs += int(counter/ 2)
            counter = 1
    return numPairs
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
