import datetime
start_time=datetime.datetime.now()
#O(n) solution
ar,k=sorted(set(map(int,input().rstrip().split()))),int(input())
#print(ar)
#temp=set([])
for i in ar:
    if abs(i-k) in ar:
        print((i,abs(i-k)),end=" ")
end_time = datetime.datetime.now()
total=end_time-start_time
print("{:.3f}".format(total.total_seconds()*1000))

"""
O(nlog(n)) Solution

def binary_search(arr,l,r,x):
    if l<=r:
        mid=(l+r)//2
        if arr[mid]==x:
            return arr[mid]
        elif arr[mid]<x:
            return binary_search(arr,mid+1,r,x)
        else:
            return binary_search(arr,l,r,x)
    else:
        return -1
ar,k=sorted(set(map(int,input().rstrip().split()))),int(input())
for i in ar:
    if binary_search(ar,0,len(ar)-1,abs(i-k))!=-1:
        print((i,abs(i-k)),end=" ")
    else:
        continue
"""
