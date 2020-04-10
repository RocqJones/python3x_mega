"""
    The program is for practice so you can use a real db like postgresql or sqlite
    - Account is a base class.
    - Checking is a sub class. It inherits from base class.
    - We will inherit when we want to transfer amount
"""
class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    # write changes to the file
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = (self.balance - amount)-self.fee
        # write the funds to account 2
        with open("account2.txt", 'w') as file:
            file.write(str(amount))


# # create and instance of an object
# account = Account("account1.txt")
# print(f"Balance: Ksh. {account.balance}")
# account.withdraw(100)
# account.commit()
# print(f"Balance: Ksh. {account.balance}")
# account.deposit(1000600)
# account.commit()
# print(f"Balance: Ksh. {account.balance}")

# # Transfering
# checking = Checking("account1.txt", 1)
# checking.transfer(899)
# print(f"Balance: Ksh. {checking.balance}")
# checking.commit()