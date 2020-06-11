def divisibleSumPairs(n, k, ar):
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if((i<j) and ((ar[i]+ar[j])%k==0)):
                cnt+=1
    return cnt
nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().split()))
result = divisibleSumPairs(n, k, ar)
print(result)
