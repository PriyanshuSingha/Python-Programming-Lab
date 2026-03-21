def count_digits(n):
    if n==0:
        
      return 0
  
    else:
        return 1+count_digits(n//10)
num=int(input("enter the number:"))
print("no of digits:",count_digits(num))                                                                                                                                                                                    