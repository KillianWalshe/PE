import numpy as np
ar=list(range(1,200))
print(ar)
Pc=0
arj=list(range(1,200))
for i in range (1,200):
    j=1
    count=0
    while arj[j]<ar[i]:
        if(ar[i-1]%arj[j]==0  and count<=1):
            count+=1
                #print("i= %d j= %d"%(i,j))
                #print(count)
            j+=1
        elif(count>1):
            #ar.pop(i-1)            
            #j=1
            break
        else:
            j+=1

    
    
    if(count==1):
        print(ar[i-1])
        Pc+=ar[i-1]

    for n in ar:
        if n%i==0: 
            break

print(Pc)          


