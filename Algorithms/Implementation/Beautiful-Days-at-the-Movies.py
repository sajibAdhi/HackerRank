#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#


def reverseNumber(number):
    # Initiate value to null
    revs_number = 0

    # reverse the integer number using the while loop

    while (number > 0):
        # Logic
        remainder = number % 10
        revs_number = (revs_number * 10) + remainder
        number = number // 10
    return revs_number


def beautifulDays(i, j, k):

    # Beautiful Days Counter
    beautiful_days = 0

    # run throw i to j
    for x in range(i, j+1):
        sub = abs(x - reverseNumber(x))
        if (sub % k) == 0:
            beautiful_days += 1

    return beautiful_days


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
