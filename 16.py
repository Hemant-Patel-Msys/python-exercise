def multiply(num1:int, num2:int)->int:
    p = 0
    for i in range(num2):
        p += num1
    return p

num1 = 60
num2 = 40

m = multiply(num1, num2)
print(m)