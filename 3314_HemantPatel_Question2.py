class Number:
    def __init__(self):
        self.sum = 0
        pass
    def add_digits(self,num):
        self.num = num
        sum = 0
        while num > 0:
            rem = num % 10
            sum = sum + rem
            num = num // 10
        sum1 = 0
        if sum < 10:
            return sum
        else:
            return self.add_digits(sum)






n = Number()
print(n.add_digits(999910))



