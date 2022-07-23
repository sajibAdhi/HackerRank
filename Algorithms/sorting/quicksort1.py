#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    middle = arr[0]
    left = []
    right = []
    newarr = []
    for i in range(1,len(arr)):
        if arr[i] > middle: right.append(arr[i])
        else: left.append(arr[i])
    newarr.extend(left)
    newarr.append(middle)
    newarr.extend(right)
    return newarr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
