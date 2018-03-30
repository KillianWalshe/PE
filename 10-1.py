import numpy as np
import timeit
start_time = timeit.default_timer()
ar=list(range(1,200000))
#print(ar)
Pc=0
for i in range (1,200000):
    j=1
    count=0
    while j<i:
        if(ar[i-1]%j==0  and count<=1):
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
        #print(ar[i-1])
        Pc+=ar[i-1]
       

print(Pc)          
elapsed = timeit.default_timer() - start_time
print(elapsed)


