x,y,z=int(input()),int(input()),int(input())
maxi=x if (x>y and x>z) else (y if (y>x and y>z)else z) 
print(" X:{} \n Y:{} \n Z:{} \n Max:{}".format(x,y,z,maxi))
