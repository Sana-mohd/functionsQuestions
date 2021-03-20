list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
#new_list = [1, 2, 5, 10, 12, 13, 16, 20] 
i=0
while i<len(list2):
    a=list2[i]
    if a  not in list1:
        list1.append(a)
    i=i+1
list1.sort()
print(list1)
    