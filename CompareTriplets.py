def compareTriplets(a, b):
    alice=0
    bob=0
    for x,y in zip(a,b):
        if x>y:
            alice+=1
        elif y>x:
            bob+=1
    return alice,bob
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result1,result2 = compareTriplets(a,b)
print(result1,result2,sep=" ")
