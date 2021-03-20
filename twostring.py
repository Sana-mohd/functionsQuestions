def string_fun(st1,st2):
    if len(st1)>len(st2):
        print(st1)
    elif len(st1)==len(st2):
        print(st1\n st2)
    else:
        print(st2)
st1=input("enter your letter: ")
st2=input("enter your letter: ")
string_fun(st1,st2)