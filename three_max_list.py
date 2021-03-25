def Nmaxelements(list1, N):
    final_list = []
    i=0
    while i<N:
        maxi=0
        j=0
        while j<len(list1):
            if list1[j]>maxi:
                maxi=list1[j]
            j=j+1
                  
        list1.remove(maxi)
        print(maxi)
        #final_list.append(maxi)
        i=i+1
        
    #print(final_list)
  
# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2
  
# Calling the function
Nmaxelements(list1, N)