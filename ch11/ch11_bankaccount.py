

class BankAccount():
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self):
        return self.balance

ac0 = BankAccount()
print(ac0.balance)
ac0.deposit(100)
ac0.withdraw(30)
print(ac0.get_balance())
ac1 = BankAccount()
ac1.deposit(1000)
print(ac1.get_balance())

print(type(BankAccount.deposit))
print(BankAccount.__init__)

print(type(ac0.deposit))
print(type(ac0.__init__))
print(BankAccount)
print(callable(BankAccount))


