#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def roundGrade(grade):
    mult = grade//5
    mult = mult + 1
    mult = mult*5
    reminder =  mult - grade
    if(reminder < 3):
        return mult
    else:
        return grade
        
        
def gradingStudents(grades):
    rounded = []
    for grade in grades:
        if(grade<38):
            rounded.append(grade)
        else:
            rounded.append(roundGrade(grade))
    return rounded

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
