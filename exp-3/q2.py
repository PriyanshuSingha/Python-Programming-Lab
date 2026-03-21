import math
co1 = int(input("enter the coeffcient:"))
co2 = int(input("enter the coeffcient:"))
co3 = int(input("enter the coeffcient:"))
d=co2**2-4*co1*co3
if d>0:
    root1=(-cof2+sqrt(d))/(2*co1)
    root2=(-cof2-sqrt(d))/(2*co1)
    print("the real roots are ",root1,"and",root2)