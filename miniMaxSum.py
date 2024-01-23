#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter and returns 
# two space-separated long integers denoting the respective minimum and maximum values 
# that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.).
#

def miniMaxSum(arr):
    arr = sorted(arr)
    print(sum(arr[:-1]), " ", sum(arr[1:]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
