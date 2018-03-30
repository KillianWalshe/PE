#What is the 10 001st prime number?


def prime(num):
    #print(pot)
    Pc=0
    for i in range(2,110000):
         j=1
         count=0
         lim=i
         maxi=i
         while j<i:
            if(i%j==0  and count<=1):
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
            Pc+=1
            if(Pc==num):
                print("The %dst prime is %d"%(num,i))
                break

    return('True')

prime(10001)
