def list_1(list=[3,5,6,9]):
    i=0
    lis=[]
    while i<len(list):
        a=list[i]
        lis.append(a)
        i=i+1
    return lis,i
print(list_1())