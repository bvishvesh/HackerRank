"""
Program to print Matrix in Wave Form 
"""
n,arr,temp,j=int(input()),[],[],0
for _ in range(n):arr.append(list(map(int,input().split())))
while(j<n):
    if(j%2==0):
        for i in range(n):temp.append(arr[i][j%n])
    else:
        for i in reversed(range(n)):temp.append(arr[i][j%n])
    j+=1
print(*temp)
