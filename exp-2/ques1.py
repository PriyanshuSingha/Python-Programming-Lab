p=int(input("enter the p:"))
r=int(input("enter the r:"))
t=int(input("enter the t:"))

Si=p*t*r/100
print("the simple interest is:",Si)
Ci=p*((1+r/100)**t)-p
print("the compound interest is:",Ci)