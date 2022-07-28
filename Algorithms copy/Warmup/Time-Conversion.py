#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    hour = str(s[0:2])
    minu = str(s[3:5])
    sec = str(s[6:8])
    day = str(s[8:10])

    if(day == 'AM'):
        if(int(hour) == 12):
            militaryTime = ("00:"+minu+":"+sec)
        else:
            militaryTime = (hour+":"+minu + ":"+sec)
    elif(day == 'PM'):
        if(int(hour) < 12):
            hour = int(hour) + 12
            militaryTime = (str(hour)+":"+minu+":"+sec)
        else:
            militaryTime = (hour+":"+minu + ":"+sec)
    return militaryTime


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
