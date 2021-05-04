#!/bin/python3

import math
import os
import random
import re
import sys
from dateutil import parser
# Complete the time_delta function below.
def time_delta(t1, t2):
    d1=parser.parse(t1.strip())
    d2=parser.parse(t2.strip())
    return str(abs(int((d2-d1).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
