def miniMaxSum(arr,size):
    arr.sort()
    totalmin=0
    totalmax=0
    for mina in range(size-1):
        totalmin+=arr[mina]
    for maxm in range(1,size):
        totalmax+=arr[maxm]
    return str(totalmin),str(totalmax)
arr = list(map(int,input().split()))
size=len(arr)
mi,ma=miniMaxSum(arr,size)
print(mi+' '+ma)
