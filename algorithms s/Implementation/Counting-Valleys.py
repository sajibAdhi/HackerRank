#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    oldPos = None
    newPos = 0
    vally = 0
    for i in range(steps):
        oldPos = newPos
        if (path[i] == 'D'):
            newPos = newPos - 1
        else:
            newPos = newPos + 1
        if(newPos == 0) and (oldPos is not None) and (oldPos < newPos):
            vally = vally +1
    return vally
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
 
