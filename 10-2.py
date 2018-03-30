import numpy as np
ar=np.arange(1,200)
print(ar)
Pc=0
for i in range (1,200):
    j=1
    count=0
    while j<i:
        if(ar[i-1]%j==0  and count<=1):
            count+=1
                #print("i= %d j= %d"%(i,j))
                #print(count)
            j+=1
        elif(count>1):
                #print("else i= %d j= %d"%(i,j))
            break
        else:
            j+=1
    
    if(count==1):
        print(ar[i-1])
        Pc+=ar[i-1]
print(Pc)          


