lst=[]
n= int(input("enter thne number of elements:"))
for i in range(n):
    lst.append(int(input()))
    lst = list(set(lst))
    lst.sort()
    print("sorted list",lst)