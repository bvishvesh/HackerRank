
def bonAppetit(bill, k, b):
    total=sum(bill)-bill[k]
    shared=int(total/2)
    if(shared!=b):
        return abs(b-shared)
    if(shared==b):
        return str("Bon Appetit")
nk = input().rstrip().split()
n = int(nk[0])
notshared=int(nk[1])
bill=list(map(int, input().split()))
charged= int(input().strip())
print(bonAppetit(bill,notshared,charged))
