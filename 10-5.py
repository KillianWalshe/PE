import numpy as np
import timeit
start_time = timeit.default_timer()
num=20000
ar=np.arange(2,num)
elapsed = timeit.default_timer() - start_time
#print(ar)
Pc=0
print(len(ar))
def poppin(ar,i):
    n=0
    for k in range(0,len(ar)):
        #print("k=%d i=%d"%(k,i))
        if(ar[i]!=0):
            x=k*ar[i]
            #print(x)
            if x<len(ar):
                ar[x-2]=0
                #print(ar)
    return (ar)
for i in range(0,num-2):
    if ar[i]==0:
        break
    else:
        j=1
        count=0
        while j-2<i:
            if(ar[i]%j==0  and count<=1):
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
            #print(ar[i])
            Pc+=ar[i]
        #print(ar)
        ar=poppin(ar,i)
    #print(ar)
    
    
       

print(Pc)          


# code you want to evaluate
elapsed1 = timeit.default_timer() - start_time
print(elapsed)
print(elapsed1)
