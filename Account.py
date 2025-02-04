class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_number = acc

    #debit method
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Amount deducted: {amount}")
            print(f"Total Balance: {self.get_balance()}")
        
    #credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Amount credited: {amount}")
        print(f"Total Balance: {self.get_balance()}")

    def get_balance(self):
        return self.balance

acc1 = Account(0,12345)
print (acc1.balance)
print (acc1.account_number)

acc1.credit(5000)

acc1.debit(3000)

acc1.credit(1000)