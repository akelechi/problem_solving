#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    maxFreq = 0
    counter = 0
    currentVal = arr[0]
    arr = sorted(arr)
    typeID = arr[0]

    for i in range(len(arr)):
        if arr[i]==currentVal:
            counter+=1
            if i == len(arr)-1:
                [counter, maxFreq, typeID] = compare_vals(counter, maxFreq, arr, typeID, i)
        else:
            [counter, maxFreq, typeID] = compare_vals(counter, maxFreq, arr, typeID, i)
            counter = 1
            currentVal = arr[i]
        print(counter)
    return typeID
def compare_vals(counter, maxFreq, arr, typeID, i):
    if counter > maxFreq:
        maxFreq = counter
        typeID = arr[i-1]
    elif counter == maxFreq:
        typeID = min(typeID, arr[i-1])
    return [counter, maxFreq, typeID]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
