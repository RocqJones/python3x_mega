import json
import random
from account import Account
from account import Checking

# transfer fee
transfer_fee = 55

# connect to backend by creating instance of an object
account = Account("account1.txt")
checking = Checking("account1.txt", transfer_fee)

def bank_activities():
    print("\nWelcome, press: \n1: Balance query.\n2: Deposit.\n3: Withdraw amount.\n4: Transfer to other account.\n")

    option = int(input("Option ? "))
    
    if option == 1:
        print(f"Balance: Ksh. {account.balance}")
        continue_or_exit()

    elif option == 2:
        dep_amount = int(input("Deposit Ksh. "))
        account.deposit(dep_amount)
        account.commit()
        print(f"Your current balance is: Ksh. {account.balance}")
        transaction_id = random.randint(10000,30000)
        print(f"Thank you for banking with us.\nTransaction ID:{transaction_id}")

    elif option == 3:
        print(f"Account balance is: Ksh. {account.balance}\n")
        wit_amount = int(input("Withdraw to MPESA(self) Ksh. "))
        account.withdraw(wit_amount)
        account.commit()
        transaction_id = random.randint(30000,60000)
        print(f"Thank you for banking with us. Your bank balance is: Ksh. {account.balance}\nTransaction ID:{transaction_id}")

    elif option == 4:
        print(f"Account balance is: Ksh. {checking.balance}\n")
        trans_amount = int(input("Transfer to other account Ksh. "))
        checking.transfer(trans_amount)
        checking.commit()
        transaction_id = random.randint(60000,90000)
        print(f"Thank you for banking with us. Your bank balance is: Ksh. {checking.balance}\nTransaction ID:{transaction_id}")


def register_user():
    print("\nCreate a new account\n")
    user_name = input("Enter Username: ")
    user_email = input("Enter Email: ")
    user_phone = input("Enter Phone (254 ...): ")
    user_password = input("Enter new password:")

    with open("profileDetails.json", 'a') as file:
        file.write("\n"+user_name+ "\t"+user_email + "\t+"+user_phone + "\t"+user_password)

    for symbol in "***************************************************************************":
        print(symbol*2)

    # call activity methods here
    bank_activities()
    continue_or_exit()


def login_user():
    print("\nPlease login first.\n")
    username = input("Username: ")
    password = input("Password: ")

    with open("profileDetails.txt", 'r') as file:
        file.seek(0)
        content = file.read()
        # print(content)
        if username in content and password in content:
            # call activity methods here
            bank_activities()
            continue_or_exit()

        else:
            print("Invalid")

def continue_or_exit():
    menu_q = input("\nDo you wish to return to menu Y/N ? ")
    menu_q.lower()
    if menu_q == "y":
        bank_activities()
    else:
        print("\nThank for banking with us.")

# commandline interface
print("WELCOME TO ROCQJONES BANK\nPlease proceed:\n1: Register.\n2: Login.\n")

option = ""

while option != 1 and option != 2:
    try:
        option = int(input("Enter option: "))

    except:
        print("Enter valid input!!!")

    else:
        if option == 1:
            register_user()

        elif option == 2:
            login_user()