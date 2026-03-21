lst=["banana","orange","apple","mango"]
for i in lst[::-1]:
    print("the reverse list is:",i)
    print("the length of each element",len(i))
rev_lst=[]
rev_lst.append(lst[::-1])
print("the reverse of each fruit name:",rev_lst)
    