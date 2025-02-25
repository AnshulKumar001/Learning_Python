class Account:
    def __init__(self, bal, acc):  # Correct constructor method
        self.balance = bal
        self.account_no = acc

    # Debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance:", self.get_balance())

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance:", self.get_balance())

    def get_balance(self):
        return self.balance


# Create an instance of Account
acc1 = Account(20000, 12345)
acc1.debit(1000)  # Debit Rs. 1000
acc1.credit(500)  # Credit Rs. 500
