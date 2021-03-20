def add_num_list(list1,list2):
    i=0
    sum=0
    while i<len(list1):
        def add_numbers():
            sum=list1[i]+list2[i]
            print(sum)
        add_numbers()
        i=i+1
add_num_list([1,2,3],[4,5,6])