a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
c=int(input("enter 3rd num:"))

max_num = max(a,b,c)
min_num = min(a,b,c)

while min_num !=0:
    remainder = max_num % min_num
    max_num = min_num
    min_num = remainder
    
    print("the gcd of three numbers are",max_num)