#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    lastEle = arr[n-1]
    endLoop = False
    for i in range(n-1,-1,-1):
        if i == 0 and endLoop != True:
            arr[i] = lastEle 
        elif arr[i-1] > lastEle :
            arr[i] = arr[i-1]
        elif arr[i-1] < lastEle:
            arr[i] = lastEle
            endLoop = True
        print(*arr)
        if(endLoop): break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
