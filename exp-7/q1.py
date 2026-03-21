m=int(input("enter the no:"))
n=int(input("enter the no:"))
for i in range(m,n):
    lst=[i]
    list(lst)
    print(lst)
print("the sum is",sum(lst))
print("the average is",(m+n/2))
print("the largest no is",max(lst))
print("the smallest no is",min(lst))
lst2=[]
for i in range(m,n):
  if  i%3==0:
    lst2.append(i)
    print(lst2)
   
        