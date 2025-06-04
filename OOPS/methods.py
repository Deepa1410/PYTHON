class rect:
    def set_dim(self,w,h):
        self.w=w  
        self.h=h 
    def area(self):
        print("area",(self.w*self.h))
    def peri(self):
        print("peri",(2*self.w+self.h))
        
        
        
l=[]
n=int(input("Enter the num of Rectangles"))
for i in range(n):
    r=rect()
    w=int(input("Enter the widht of Rect{}".format(i+1)))
    h=int(input("Enter the height of the Rect{}".format(i+1)))
    r.set_dim(w,h)
    l.append(r)
for i in range(n):
    print("RECTANGLE NUM{}".format(i+1))
    l[i].area()
    l[i].peri()
    print("-------------------")
print(l)   
