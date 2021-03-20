def fib(n):
    a= 0
    b=1
    while a < n:
        s=a
        a= b
        b=a+b
    return s
    print()
print(fib(10))