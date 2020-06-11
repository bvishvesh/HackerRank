
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applecount=0
    orangecount=0
    for i in range(len(apples)):
        apples[i]+=a
        if(apples[i]>=s and apples[i]<=t):
            applecount+=1
    for j in range(len(oranges)):
        oranges[j]+=b
        if(oranges[j]>=s and oranges[j]<=t):
            orangecount+=1
    return int(applecount),int(orangecount)

st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
app,org=countApplesAndOranges(s, t, a, b, apples, oranges)
print(app,org, sep='\n')
