d1={}
n= int(input("enter the no key value pair:"))
for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    d1[key]=value
d2={}
for key,value in d1.items():
    d2[value]=key
    print("original dictionary:",d1)
    print("dict after swapping keys and values:",d2)    