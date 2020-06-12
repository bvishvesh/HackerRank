def hurdleRace(k, height):
    if(max(height)<=k):
        return 0
    else:
        return max(height)-k
nk = list(map(int,input().split()))
n = nk[0]
k = nk[1]
height = list(map(int, input().rstrip().split()))
print(hurdleRace(k, height))
