#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    A = sorted(A, reverse=True)
    B = sorted(B)
    C = []
    C_2 = []
    print(A)
    print(B)
    
    for elem1, elem2 in zip(A, B):
        C.append(elem1 + elem2)
    C = sorted(C)
    print(C)
    
    A = sorted(A)
    B = sorted(B, reverse=True)
    print(A)
    print(B)
    
    for elem1, elem2 in zip(A, B):
        C_2.append(elem1 + elem2)
    C_2 = sorted(C_2)
    print(C_2)
    if (C[0] >= k) | C_2[0]>=k:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
