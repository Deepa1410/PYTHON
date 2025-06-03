def abc(n,c):
    if n == 4:
        return 1
    c = c+1 
    b = abc(n+1,c)
    print(c,end=" ")
    return b*2
print(abc(1,1)) 
