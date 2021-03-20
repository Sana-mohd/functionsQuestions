#making of split function 
string="my name  hhhh fgdgd ffdhf is sana"
def split_fun(string):
    i=0
    list=[]
    while i<len(string):
        new=""
        j=i
        while j<len(string):
            if string[j]==" ":
                #list.append(new)
                break
            else:
                new=new+string[j]
            j=j+1
        list.append(new)
        i=j+1
    print(list)
split_fun(string)
