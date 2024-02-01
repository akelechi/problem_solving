#!/bin/python3

import math
import os
import random
import re
import sys



def lonelyinteger(a):
    sorted_array = sorted(a)
    lengthofArr = len(a)
 
    if lengthofArr > 1:
        for i in range(lengthofArr):
            if i == 0:
                if sorted_array[i]!=sorted_array[i+1]:
                    return sorted_array[i]
            elif (i>0) & (i<lengthofArr-1):
                if (sorted_array[i]!= sorted_array[i-1]) & (sorted_array[i]!= sorted_array[i+1]):
                    return sorted_array[i]
            elif i == lengthofArr-1:
                return sorted_array[i]
    
    return sorted_array[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
