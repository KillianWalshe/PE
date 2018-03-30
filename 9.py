#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

for i in range (1,500):
    for j in range(i,500):
        for k in range (1000-j-i,1000):
            if (i**2+j**2==k**2):
                if(i+j+k==1000):
                    print(i*j*k)
                    
