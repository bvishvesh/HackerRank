def aVeryBigSum(ar):
    return sum(ar)
ar_count = int(input())
ar = list(map(int, input().strip().split()))
result = aVeryBigSum(ar)
print(result)
