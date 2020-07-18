#!/bin/python3
import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    arr = arr.copy()
    sorted_arr = sorted(arr)

    def swap(a,b):
        arr[a],arr[b] = arr[b],arr[a];
        nonlocal swaps 
        swaps += 1

    while arr != sorted_arr:
        for element,ideal in zip(arr,range(1,len(arr)+1)):
            element_should_be = element - 1
            element_index = ideal - 1
            if element != ideal:
                swap(element_should_be,element_index)
    return swaps
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
