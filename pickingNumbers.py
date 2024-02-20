#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    multiple = b[0]
    factor = a[0]
    for i in range(len(b)):
        multiple = math.gcd(multiple, b[i])
    
    for j in range(len(a)):
        factor = math.lcm(factor, a[j])
    
    if multiple/factor == 1:
        return 1
    else:
        quotient = multiple/factor
        pfs = primeFactors(quotient)
        counter = 1 + len(pfs)
        return counter

def primeFactors(n):
    arr = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        arr.append(2)
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n))+1, 2):
         
        # while i divides n , print i and divide n
        while n % i== 0:
            arr.append(i)
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        arr.append(n)

    return arr
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
