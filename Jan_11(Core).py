#----------Base class-----------
class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount ):
        self.amount = amount
        self.balance+=self.amount
        print(f"Depositing.... {self.amount}")
        print("Deposite successful.")

    def show_balance(self):
        print(f"Current balance: {self.balance}")


#-------------Child class-----------------
class SavingsAccount(BankAccount):
    def __init__(self, balance, account_holder):
        super().__init__(balance, account_holder)    
    
    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        self.balance-= self.withdraw_amount
        print(f"Withdrawing.... {withdraw_amount}")
        print("Withdraw successful.")


#-----------------------inputs-----------------------
account_holder = input("Enter Account holder's name: ")
balance = int(input("Enter initial balance: "))



#----------------function call------------------
account1 = SavingsAccount(account_holder, balance)
print("*" * 50)

account1.show_balance()
print("\n")
account1.deposit(100)
print("\n")
account1.withdraw(1)
print("\n")
account1.show_balance()



        


