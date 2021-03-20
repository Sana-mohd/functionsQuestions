question_list=["how many continents are there in the world?","what is the capital city of india?","who invented computer?","identify which place belongs to telangana?","identify which is proper noun?"]
options_list=[["four","nine","seven","eight"],["hyderabad","bhopal","sikkim","delhi"],["charles babbage","thomas","issac newton","euler"],["lucknow","golconda","rayala seema","nandi hills"],["car","laptop","new york","mountain"]]
solution=["seven","delhi","charles babbage","golconda","new york"]

def answer():
    j=0
    while j<len(solution):
        if user_answer==solution[j]:
            print("congratulations")
            break
        j=j+1
import random
def life_line(i):
    k=i
    a=[]
    while k<len(options_list):
        z=0
        while z<len(options_list[k]):
            if options_list[k][z] in solution:
                a.append(options_list[k][z])
                options_list[k].pop(z)
                a.append(random.choice(options_list[k]))
                print(a)
                user1=input("enter your answer: ")
                if user1==solution[k]:
                    return "congratulations"
                else:
                    return "sorry you lost"
                
            z=z+1
            
        k=k+1
        
def kbc():
    print("welcome to the game\nlet us start the game")
    lifeline=1
    i=0
    while i<len(question_list):
        print(question_list[i])
        print(options_list[i])
        global user_answer
        user_answer=input("enter your answer: ")
        if user_answer=="50-50":
            #global lifeline
            if lifeline==1:
                lifeline=lifeline+1
                print( life_line(i))
            elif lifeline>1:
                print("you have used a lifeline .so, there are no lifeline")
                print(options_list[i])
                user_answer=input("enter your answer: ")
                if user_answer==solution[i]:
                    print("congratulations")
                else:
                    print(" you loose the game" )
                    break
        elif user_answer not in solution:
            print("you answer is wrong\nquit the game")
            break
        answer()
        i=i+1
kbc()


