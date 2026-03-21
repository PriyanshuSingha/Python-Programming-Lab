n=int(input("enter the no:"))
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
      if n <= 1 and n % i == 0:
        print("not prime")
      else:  
        print("prime")
is_prime(n)