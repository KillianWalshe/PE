import timeit
start_time = timeit.default_timer()
num=2000000
#ar=arange(1,num)
#print(ar)
Pc=0


def isprime(x):
    if(x%2==0):
        return(0)
    else:    
        p=3
        while p<x**0.5+1:
            if(x%p==0):  
                return(0)       
            else:
                p+=2      

        return (x)

summ=1
for i in range(0,num):
    summ+=isprime(i)
print(summ)



# code you want to evaluate
elapsed = timeit.default_timer() - start_time
print(elapsed)

