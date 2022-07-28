#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    largest = None;
    numOfCandle = 0;
    for candle in candles:
        if(largest is None):
            numOfCandle = 1;
            largest = candle
        elif( largest < candle):
            numOfCandle = 1;
            largest = candle;
        elif(largest == candle):
            numOfCandle = numOfCandle + 1
    
    return numOfCandle
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
