#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    min = None
    max = None;
    minSum = 0;
    maxSum = 0;
    for num in arr:
        if num < 0 or num > ((10**9)+1):
            break
        if max is None or max < num :
            max = num;
        if min is None or min > num :
            min = num;
    maxCheck = 0
    minCheck = 0
    for num in arr:
        if(num != max or maxCheck > 0):
            minSum = minSum + num
        else: 
            maxCheck = 1
        if(num != min or minCheck > 0):
            maxSum = maxSum + num
        else: 
            minCheck = 1
    print(minSum, maxSum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
 