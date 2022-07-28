#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    billLen = len(bill)
    totalBill = 0
    for i in range(billLen):
        if(i != k):
            totalBill = totalBill + bill[i]
    annasBill = totalBill/2
    
    if(annasBill == b):
        print("Bon Appetit")
    else:
        print(int(b-annasBill))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
