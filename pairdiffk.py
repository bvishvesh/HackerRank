ar,k=sorted(set(map(int,input().rstrip().split()))),int(input())
#print(ar)
#temp=set([])
for i in ar:
    if abs(i-k) in ar:
        print((i,abs(i-k)),end=" ")
