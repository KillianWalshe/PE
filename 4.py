#A palindromic number reads the same both ways. The largest palindrome made from the product #of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.



def pal(x):
    str1=[]
    x1=str(x)
    for p in x1:
        str1.append(p)
    
#    print(x)
#    print(x1)
#    print(str1)
    str1=reversed(str1)
    str1=''.join(map(str,str1))
#    print(str1)    
#    print(int(str1))

    if(x==int(str1)):       
        #print("palindrone = %d"%x)
        return(x)
    else:
        return(0)    
    
    #int(y)
    #if(x==y):
    #    print("palindrone = %d"%x)


HP=101
P=1
for i in reversed(range(100,999)):
    for j in reversed(range(100,999)):
        #print("i= %d j= %d"%(i,j))
        k=i*j
        P=pal(k)
        if(P>HP):
            HP=P

print(HP)
