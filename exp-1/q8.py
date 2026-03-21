import math
a=int(input("enter a number a: "))
b=int(input("enter a number b: "))
c=int(input("enter a number c: "))
p=a+b+c
s=p/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"the area of the triangle is {area} and perimeter is {p}")