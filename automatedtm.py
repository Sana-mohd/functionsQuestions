def balance_enquiry():
    print("your current balance is ", user_amount)
    return "thank you for using this ATM"
def cash_withdrawl():
    user_drawl=input("enter your type of amount to withdraw: ")
    if user_drawl=="savings":
        user_cash=input("enter the amount you want: ")
        print( "collect your cash", user_cash)
        return "thank you for using this ATM"
    else:
        return "no amount in current account"
def change_pin():
    print("to change your pin number firstly enter the mobile number which is registered")
    user_number=int(input("enter your mobile number: "))
    print("enter the OTP ypu got on your mobile for changing pin")
    user_otp=int(input("enter otp: "))
    if len(user_otp)==6:
        user_newpin=int(input("enter your new pin: "))
        print("your pin has been changed ",user_newpin)
        return "thank you for using this ATM"
    else:
        return "re-enter your transaction"
def main_atm(user_amount):
    print("welcome to the ATM\nlets start our transaction")
    user_language=input("enter your language: 1.english  or the language you want: ")
    if user_language=="english":
        i=0
        while i<3:
            user_pin=input("enter your pin: ")
            if user_pin=="0376":
                user_transaction=int(input("choose the transaction you wish to do: 1.balance enquiry 2.cash withdrawl 3.change pin "))
                if user_transaction==1:
                    print(balance_enquiry())
                elif user_transaction==2:
                    print(cash_withdrawl())
                elif user_transaction==3:
                    print(change_pin())
                break
            else:
                print("your pin is wrong")
            i=i+1
        else:
            return "you has entered wrong pin 3 times\nyour card has been blocked" 
    else:
        print( " use google translator")
user_amount=input("decide the amount you have in your savings account")
main_atm(user_amount)