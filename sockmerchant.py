#!/bin/python3
import collections
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    cnt=collections.Counter(ar)
    totalpairs=0
    for k in cnt.values():
        if(k==1):
            continue
        else:
            totalpairs+=int(k/2)
    return totalpairs
n = int(input())
ar = list(map(int, input().split()))
print(sockMerchant(n, ar))
