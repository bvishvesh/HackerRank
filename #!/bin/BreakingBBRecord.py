#!/bin/python
def breakingRecords(scores):
    mini=scores[0]
    maxi=scores[0]
    minicount=0
    maxcount=0
    for i in range(len(scores)):
        if(scores[i]<mini):
            mini=scores[i]
            minicount+=1
        elif(scores[i]>maxi):
            maxi=scores[i]
            maxcount+=1
    return minicount,maxcount
n = int(input())
scores = list(map(int,input().split()))
m1,m2 = breakingRecords(scores)
print(m2,m1,sep=' ')

   
