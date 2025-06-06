def gen_fibo(x):
    a,b=0,1 
    for i in range(x):
        yield a 
        a,b=b,a+b 
for i in gen_fibo(7):
    print(i,end='')
