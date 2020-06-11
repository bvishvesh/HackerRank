
def catAndMouse(cata, catb, mouse):
    a=abs(cata-mouse)
    b=abs(catb-mouse)
    if(a==b):
        return str("Mouse C")
    else:
        mini=min(a,b)
        if(mini==a):
            return str("Cat A")
        else:
            return str("Cat B")
q = int(input())
for q_itr in range(q):
    xyz=input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    print(catAndMouse(x, y, z))
