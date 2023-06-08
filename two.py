var = lambda x: x ** 2
print(var(2))

a = lambda a, b: a + b
print(a(4, 5))

f = lambda n: 1 if n == 0 else n * f(n - 1)
print(f(5))


