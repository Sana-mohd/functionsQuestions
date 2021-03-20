def eligible_for_vote(user_age=int(input("enter your age"))):
    if user_age>=18:
        print("you are eligible to vote")
    else:
        print("your not elegible")
eligible_for_vote()