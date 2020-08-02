import datetime
start_time=datetime.datetime.now()
ar,k=sorted(set(map(int,input().rstrip().split()))),int(input())
#print(ar)
#temp=set([])
for i in ar:
    if abs(i-k) in ar:
        print((i,abs(i-k)),end=" ")
end_time = datetime.datetime.now()
total=end_time-start_time
print("{:.3f}".format(total.total_seconds()*1000))
