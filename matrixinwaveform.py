"""
Program to print Matrix in Wave Form 
"""
n = int(input())
arr,temp=[],[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
i,j=0,0
while(j<n):
    if(j%2==0):
        for i in range(n):
            temp.append(arr[i][j%n])
    else:
        for i in reversed(range(n)):
            temp.append(arr[i][j%n])
    j+=1
for i in range(len(temp)):
    print(temp[i],end="\t")
