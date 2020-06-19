#!/bin/python3
from collections import Counter
# Complete the equalizeArray function below.
def equalizeArray(arr):
    c=Counter(arr)
    maxi=max(c.values())
    return(n-maxi)
n = int(input())
arr = list(map(int, input().rstrip().split()))
print(equalizeArray(arr))

