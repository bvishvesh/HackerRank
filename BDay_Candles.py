ef birthdayCakeCandles(ar):
    return ar.count(max(ar))
ar_count = int(input())
ar=list(map(int, input().split()))
result = birthdayCakeCandles(ar)
print(result)
