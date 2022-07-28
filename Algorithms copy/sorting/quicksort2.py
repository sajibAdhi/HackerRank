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
    pivot = []
    left = []
    right = []
    
    for i in arr:
        if len(pivot) == 0:
            pivot.append(i)
        elif pivot[0] > i:
            left.append(i)
        else:
            right.append(i)
    if len(left) > 1:
        left  = quickSort(left)
    if len(right) > 1:
        right = quickSort(right)
        
    result = left + pivot +right
    fptr = open(os.environ['OUTPUT_PATH'], 'a')
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
    return result

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)
