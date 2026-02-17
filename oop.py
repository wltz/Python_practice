
class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        self.payment_amt = 0
        self.deposit_amt = 0

    def deposit(self, amount):
        self.deposit_amt += amount

    def withdraw(self, amount):
        self.payment_amt += amount

    def get_balance(self):
        return self.balance + self.deposit_amt - self.payment_amt

    def __dunder_method(self):        
        print("The double underscore is to avoid overriding by child class")

    def base_method(self):
        print("This is a base method in Account, can be overridden by child class")


class MasterAccount(Account):
    def __init__(self, id, balance):
        super().__init__(id, balance)
        self.balance = balance

    def get_balance(self):
        """
        The child class can override the parent class method.
        1. completely implement different logic
        2. call the parent class method to get the parent class 
           result, then add additional logic to it
        """
        super().get_balance()    
        print("MasterAccount balance:", self.balance)

    def __dunder_method(self):        
        print("This is a private method in MasterAccount")
        #super().__private_method()

    def base_method(self):
        #super().base_method()
        print("Override base method by child class")

if __name__ == "__main__":
    account = Account(1, 100)
    print("Account balance:", account.get_balance())
    #account.__private_method() # This will raise an AttributeError
    account._Account__dunder_method() # This will work
    master_account = MasterAccount(2, 200)
    print("MasterAccount balance:", master_account.get_balance())
    #master_account.__private_method() # This will raise an AttributeError
    master_account._MasterAccount__dunder_method() # This will work
    master_account.base_method()