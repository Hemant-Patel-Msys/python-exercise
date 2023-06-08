class Bank:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def check_bal(self):
        return self.balance


b = Bank()
while True:
    content = """
    What do you want 
    1. Check Balance 
    2. Deposit amount
    3. Withdraw the amount
    4. Exit
    """
    print(content)
    user = int(input("Enter your choice:- "))
    if user == 1:
        print("Your account balance is ",b.balance)
    elif user == 2:
        d = int(input("Enter the amount to deposit:-"))
        print(b.deposit(d))
    elif user == 3:
        w = int(input("Enter the amount to withdraw:-"))
        print(b.withdraw(w))
    elif user == 4:
        exit()