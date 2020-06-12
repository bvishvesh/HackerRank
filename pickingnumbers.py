def pickingNumbers(ar,n):
   return max(ar.count(x)+ar.count(x+1) for x in list(ar))
n = int(input().strip())
a = list(map(int, input().rstrip().split()))
print(pickingNumbers(a,n))
