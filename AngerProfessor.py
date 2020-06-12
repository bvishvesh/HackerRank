#!/bin/python3
def angryProfessor(k,a):
    cnt=0
    for _ in range(len(a)):
        if(a[_]<=0):
            cnt+=1
    if(cnt>=k):
        return str("NO")
    else:
        return str("YES")
t = int(input())
for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    a = list(map(int, input().rstrip().split()))
    result = angryProfessor(k,a)
    print(result,sep="\n")
