def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a%b
def calculator(a,b,c):
    if c=="+":
        print(add(a,b))
    elif c=="_":
        print(sub(a,b))
    elif c=="*":
        print(mul(a,b))
    elif c=="%":
        print(div(a,b))
a=int(input("enter your num: "))
b=int(input("enter your num: "))
c=input("enter your sign: ")
calculator(a,b,c)