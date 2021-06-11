#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if( 0 < len(s) and len(s) < 1000):
        result = None
        words = s.split(' ')
        for word in words:
            if( result is None):
                result = word.capitalize()
            else: result = result + ' ' + word.capitalize()
            # print(word.capitalize())
    return result
if __name__ == '__main__':