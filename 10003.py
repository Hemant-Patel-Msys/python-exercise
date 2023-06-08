class Bank():
    def __init__(self,name='a',id=1,balance = 0):
        self.name = name
        self.id = id
        self.balance = balance



class Operation(Bank):

    def add_money(self,amount):
        self.balance = self.balance + amount
        return self.balance
    def withdrawal_money(self,amount):
        self.balance =self.balance - amount
        return self.balance






c = Bank('A',1)
o = Operation()
print(c.balance)
print(o.add_money(100))
print(o.withdrawal_money(50))
print(o.balance)