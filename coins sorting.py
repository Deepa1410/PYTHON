coins=[2,5,10,200,20,500,100,50,1]
amount=int(input("Enter the Amount"))
a=sorted(coins,reverse=True)
while amount != 0:
    for i in a:
        if amount >=i:
            print(i,end=" ")
            amount=amount-i
            break
