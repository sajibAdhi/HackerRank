#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    maxScore = None
    minScore = None
    maxScoreBreak = 0
    minScoreBreak = 0

    for score in scores:
        if(maxScore is None):
            maxScore = score
        elif(maxScore < score):
            maxScore = score
            maxScoreBreak = maxScoreBreak + 1

        if(minScore is None):
            minScore = score
        elif(minScore > score):
            minScore = score
            minScoreBreak = minScoreBreak + 1
    return [maxScoreBreak, minScoreBreak]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
