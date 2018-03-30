def sums(x):
    sum=0
    for i in range(1,x+1):
        sum+=i
        
    return(sum**2)
def squareds(x):
    ss=0
    for i in range(1,x+1):
        s=i**2
        ss+=s
    return(ss)

print(sums(100))
print(squareds(100))
print(sums(100)-squareds(100))    
