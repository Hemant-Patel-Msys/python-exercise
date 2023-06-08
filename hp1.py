class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        for i in self.ingredients:
            a =[i] + self.toppings
            print(a,end="")




if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops())  # should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]