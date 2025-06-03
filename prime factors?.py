def prime(a):
    i=2
    if(a==1):
        return
    while(a%i !=0):
        i=i+1 
    print(i,end=" ")
    prime(a//i)
n=int(input("Enter any num"))
prime(n)
