a, b = 0, 1
fib = []


while a <= 1000:
    fib.append(a)
    a, b = b, a + b

print("Fibonacci series up to 1000:", fib)


sum_even = 0
for x in fib:
    if x % 2 == 0:
        sum_even += x

print("Sum of even Fibonacci numbers:", sum_even)