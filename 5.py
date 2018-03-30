#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

match=0
while match==0:
    for num in range(1,1000000000):
        count=0
        for i in range (1,21):
            if(num%i==0):
                #print(count)
                count+=1                                 
                if(count==20):
                    print(num)
                    match=1
                    break
            else:
                break
    print("out of range")
    break                 
