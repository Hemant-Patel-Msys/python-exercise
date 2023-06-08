class Test:
    def __init__(self):
        pass
    def get_data(self):
        return "Fetch data from database"
    def t1(self):
        return self.get_data()
    def t2(self):
        return self.get_data()
t = Test()
print("Before Monkey Patching")
print(t.t1())
print(t.t2())
def new_get_data(self):
    return "Fetch data from new database"
Test.get_data = new_get_data
print("After Monkey Patching")
print(t.t1())
print(t.t2())








