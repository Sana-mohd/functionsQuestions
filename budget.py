number_students=int(input("enter your total no. of students: "))
spent_on_student=int(input("enter the amount spent on one student: "))
total_budget=number_students*spent_on_student
if total_budget<=50000:
    print("hum budget me hai")
else:
    print("hum budget ke baher hai")