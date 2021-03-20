list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
list=[]
i=0
while i<len(list1):
    a=list1[i]
    j=0
    while j<len(list2):
        b=list2[j]
        if a ==b:
            list.append(a)
        j=j+1
    i=i+1
list.sort()
print(list)

        
#new_list = [1, 23, 75, 98] 