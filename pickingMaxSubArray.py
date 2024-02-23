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
    countOfSubArray = 1
    maxCount = 0
    pivot = a[0]
    pivotPosition = 0
    a = sorted(a)
    for i in range(1, len(a)):
        if a[i]-pivot<2:
            countOfSubArray +=1
            if (i == len(a)-1) & (countOfSubArray > maxCount):
                maxCount = countOfSubArray
        else:
            if countOfSubArray > maxCount:
                maxCount = countOfSubArray
                for j in range(pivotPosition, i+1):
                    if a[i]-a[i-j] >2:
                        pivotPosition = i-j
                        countOfSubArray = 1+j
                        break
            pivot = a[pivotPosition]
        
    return maxCount
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
