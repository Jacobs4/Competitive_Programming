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
    n = len(arr)
    positive =  0
    negative = 0
    zero = 0
    if n == 0:
        print('0.000000')
        print('0.000000')
        print('0.000000')
        return
    else:
        for i in range(0,n):
            if arr[i] > 0:
                positive += 1
            elif arr[i] <  0:
                negative += 1
            else:
                zero += 1
        print('%.6f' % (positive/n))
        print('%.6f' % (negative/n))
        print('%.6f' % (zero/n))
        return
     

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
