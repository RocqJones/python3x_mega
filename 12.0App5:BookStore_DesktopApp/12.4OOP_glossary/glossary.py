"""
    The program covers; classes, object instances, instance variable, and class variable
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

    # class variable
    type = "checking"
    
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = (self.balance - amount)-self.fee
        # write the funds to account 2
        with open("account2.txt", 'w') as file:
            file.write(str(amount))


tommy_checking = Checking("tommy_ac.txt", 1) # instantiation
tommy_checking.transfer(100)
print(f"Balance: Ksh. {tommy_checking.balance}")
tommy_checking.commit()
print(tommy_checking.type) # 'type' is an attribute

jimmy_checking = Checking("jimmy_ac.txt", 1) # instantiation
jimmy_checking.transfer(250)
print(f"Balance: Ksh. {jimmy_checking.balance}")
jimmy_checking.commit()
print(jimmy_checking.type)