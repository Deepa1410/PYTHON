name="ABCDEFGHIJ"
names=[i for i in str(name)]
salary=[10000,20000,12000,55000,45000,20000,26000,60000,17000,25000]
memo=[0,1,1,1,2,3,2,0,2,2]
a=list(zip(names,salary,memo))
removed=[i for i in a if i[1]>40000]
bal=[i for i in a if i[1]<=40000]
bal.sort(key=lambda x: x[1],reverse=True)
to_remove=[]
for i in bal:
    if(i[2]>=2):
        to_remove.append(i)
    if(len(to_remove)==3):
        break
final=removed+to_remove
x=1
for i in final:
    print("{}.{} has been removed - sal {} and memo is {}" .format(x,i[0],i[1],i[2]))
