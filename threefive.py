def shownumber(limit=int(input("enter your number: "))):
    i=0
    sum=0
    while i<=limit:
        if i%3==0 or i%5==0:
            print(i, "multiple")
            sum=sum+i
        i=i+1
    print(sum)
shownumber()
        
    