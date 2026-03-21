num=int(input("enter the number:"))
num_str=str(num)

if num_str ==  num_str[::-1]:
    print("the number is palindrome")
else:
    print("the number is not palindrome")    