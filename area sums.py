def circle():
    c=int(input("Enter the radius of the circle"))
    print("Area of circle is",3.14*c*c)
def rect(l,b):
    print("Area of rectangle is",l*b)
def tri():
    b=(int(input("Enter the base of the triangle")))
    h=(int(input("Enter the height of the triangle")))
    return 0.5*b*h 
def squ(a):
    return a*a 
    
while (True):
    print("1.CIRCLE")
    print("2.RECTANGLE")
    print("3.TRIANGLE")
    print("4.SQUARE")
    print("5.EXIT")
    d=int(input("Enter Your Choice"))
    match d:
        case 1:
            circle()
        case 2:
            l=int(input("Enter the Lenght of the rectangle"))
            b=int(input("Enter the Breadth of the rectangle"))
            rect(l,b)
        case 3:
            res=tri()
            print("Area of tri is",res)
        case 4:
            a=int(input("Enter the side of the square"))
            res1=squ(a)
            print("Area of square is",res1)
        case 5:
            break
        case _:
            print("Invalid")
            
