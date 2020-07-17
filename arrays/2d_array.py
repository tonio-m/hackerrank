#!/bin/python3
import math
import os
import random
import re
import sys


def hourglassSum(arr):
    results = list()
    k = -1
    for i in range(16):
        j = i % 4
        if j == 0: k += 1
        hourglass = [
                arr[k][j], arr[k][j+1], arr[k][j+2],
                arr[k+1][j+1],
                arr[k+2][j], arr[k+2][j+1], arr[k+2][j+2]
        ]
        results.append(sum(hourglass))
    return max(results)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
    arr = []
 
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
 
    result = hourglassSum(arr)
 
    fptr.write(str(result) + '\n')
 
    fptr.close()

