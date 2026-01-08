'''

'''

class BankAccount:

    def __init__(self):
        self.__balance = 0

    def valid_amt(self, amt):
        if amt < 0:
            raise Exception("Invalid Amount")
        return True
    
    def deposit(self, amt):
        if self.valid_amt(amt):
            self.__balance += amt
    
    def check_balance(self, amt):
        if self.valid_amt(amt):
            return amt < self.__balance
    
    def withdraw(self, amt):
        if self.check_balance(amt):
            self.__balance -= amt
            return
        raise Exception("Insufficient balannce")
    
    def get_balance(self):
        return self.__balance

ba = BankAccount()
ba.deposit(500)
ba.withdraw(100)
print(ba.get_balance())
