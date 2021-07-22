#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    n = len(arr)
    zero = positive = negative = 0
    
    for i in arr:
        if (i == 0):
            zero = zero +1
        elif (i > 0):
            positive = positive +1
        elif (i < 0):
            negative = negative +1
    
    positive = positive / n
    negative = negative / n
    zero = zero / n
    
    formatter = '{:.6}'
    print(formatter.format(positive))
    print(formatter.format(negative))
    print(formatter.format(zero))

    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
