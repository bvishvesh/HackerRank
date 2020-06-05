def plusMinus(arr,n):
    pos,neg,neut=0,0,0
    for _ in range(n):
        if arr[_]>0:
            pos+=1
        elif arr[_]<0:
            neg+=1
        else:
            neut+=1
    return float(pos/n),float(neg/n),float(neut/n)
n = int(input())
arr=list(map(int, input().split()))
r1,r2,r3=plusMinus(arr,n)
print(float(r1),float(r2),float(r3),sep='\n')
