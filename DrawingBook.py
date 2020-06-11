#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    return min(p//2,n//2-p//2)
n = int(input())
p = int(input())
print(pageCount(n, p))
