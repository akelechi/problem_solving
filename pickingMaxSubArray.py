#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    countOfSubArray = 0
    maxCount = 0
    a = sorted(a)
    for i in range(1, len(a)):
        if a[i]-a[i-1]<2:
            countOfSubArray +=1
        else:
            if countOfSubArray > maxCount:
                maxCount = countOfSubArray
            countOfSubArray = 0
    return maxCount
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
