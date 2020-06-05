def diagonalDifference(arr,n):
    rightdiag,leftdiag=0,0
    for i in range(n):
        for j in range(n):
            if i==j:
                leftdiag+=arr[i][j]
            if i==(n-j-1):
                rightdiag+=arr[i][j]
    return abs(leftdiag-rightdiag)
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
result = diagonalDifference(arr,n)
print(result)

