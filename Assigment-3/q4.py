# q4 wap to check a string is palindrome or not.
x=input("enter a string:")
z=(str(str(x)[::-1]))
if x==z:
    print("it is a palindrome")
else:
    print("it is not a palindrome")