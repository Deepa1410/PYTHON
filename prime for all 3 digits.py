def prime(a):
    c=0 
    for i in range(2,a):
        if(a%i==0):
            c=c+1 
    return c==0 
def sum1(a):
    tot=0 
    while(a>0):
        tot=tot+a%10 
        a=a//10
    return tot    
for i in range(100,1000):
    if(prime(i) and prime(sum1(i))):
        print(i)
