import numpy as np
ar=list(range(2,26))
#print(ar)
Pc=1
print(len(ar))
def poppin(ar,i):
    n=0
    while n <len(ar):
        ar.pop(n)
        n+=i-1
        #print(ar)
while len(ar)>1:
    i=0
    j=1
    count=0
    while j<ar[i]:
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
        print(ar[i])
        Pc+=ar[i]

    poppin(ar,ar[i])
    print(ar)
    
    
       

print(Pc)          


