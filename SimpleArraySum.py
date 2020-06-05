def simpleArraySum(ar):
    return sum(ar)
ar_count = int(input())
ar=list(map(int, input().split()))
result = simpleArraySum(ar)
print(result)
