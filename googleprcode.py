//program to find the square of diagonal elements in O(n) time complexity.
li=[]
temp=[]
temp1=[]
for _ in range(int(input())):
    li.append([int(x) for x in input().split()])
for x in range(len(li)):
    y=x
    temp.append(li[x][y]**2)
print(temp)
y=(len(li)-1)
for x in range(len(li)):
    temp1.append(li[x][y]**2)
    y-=1
print(temp1)
