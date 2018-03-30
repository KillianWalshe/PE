def factors(num):
    fac=[]
    lim = num
    i = 1
    while (i <=lim):
        if num%i==0:
            lim=num/i -1
            fac.append(i)        
            #print(i)
            
        else:
            pass
        i += 1
    return(fac)



def prime(num):

    pot=factors(num) 
    HPF=1
    for i in range(len(pot)):
         j=0
         count=0
         while j<=i:
            if(pot[i]%pot[j]==0  and count<=2):
                count+=1
                j+=1
            else:
                j+=1
                
         if(count<=2 and HPF<pot[i]):
            HPF=pot[i]
                              
    return(HPF)



num = 600851475143
print(factors(num))
print(prime(num))



