# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if(v1<=v2):
        return str("NO")
    else:      
        if((x2-x1)%(v1-v2)==0):
            return str("YES")
        else:
            return str("NO")
x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
result = kangaroo(x1, v1, x2, v2)
print(result)
