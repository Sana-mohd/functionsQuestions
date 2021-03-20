#return [my_list[i] for i in range(l) if i != position]

def remove(my_list, position):
    l = len(my_list)
    new=[]
    i=0
    while i<l:
        if my_list[i]!=position:
            new.append(my_list[i])
        i=i+1
    return new
print(remove([1,"sana","python",3],"python"))