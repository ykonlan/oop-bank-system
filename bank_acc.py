class InsufficientBalance(Exception):
    def __init__(self, balance, name, *args):
        self.balance = balance
        self.name = name

    def __str__(self):
        return f"Account '{self.name}' has insufficient balance. Remaining balance is {self.balance:.2f}"

class BankAccount:
    def __init__(self,balance,name):
        self.__balance = balance
        self.name = name

    @property
    def balance(self):
        return self.__balance
         
    
    @balance.setter
    def balance(self,amount):
        if amount < 0:
            raise ValueError("Enter a valid amount")
        self.__balance = amount
        return


    def get_balance(self):
        print(f"Your available balance is {self.balance:.2f}")

    def balance_is_sufficient(self,amount):
        if amount > self.balance:
            raise InsufficientBalance(self.balance,self.name)
        return True
    
    def transfer_funds(self,amount,account):
        self.balance_is_sufficient(amount=amount)
        self.balance -= amount
        account.balance += amount
        print(f"Transaction complete✅")
        self.get_balance()
        return
    
    def withdraw_funds(self,amount):
        self.balance_is_sufficient(amount)
        self.balance -= amount
        print(f"Transaction complete✅")
        self.get_balance()
        return
    
    def deposit_funds(self,amount):
        self.balance += amount
        self.get_balance()
       

class InterestAccount(BankAccount):
    def __init__(self, balance, name):
        self.balance = (balance * 1.1)
        self.name = name


yoeman = BankAccount(1000,"Yoeman")
tiilon = BankAccount(1000,"Tiilon")

yoeman.balance= 100