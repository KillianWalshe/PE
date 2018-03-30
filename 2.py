#k=[]
k=0
a=1
b=1

while b < 4000000:
    b+=a
    if(b%2==0):   
        #k.append(b)
        k+=b
    a,b=b,a
print(k)
