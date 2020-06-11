def birthday(squares, day, month,n):
    cnt = 0
    q = squares[:month-1]
    for ele in squares[month-1:]:
        q.append(ele)
        if (sum(q) == day):
            cnt += 1
        q.pop(0)
    return cnt
n = int(input().strip())
s = list(map(int, input().rstrip().split()))
dm = input().split()
d = int(dm[0])
m = int(dm[1])
result = birthday(s, d, m,n)
print(result)
