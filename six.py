mylist=[1, 5, 9, int('0')]
print(sum(mylist))

var1 = lambda var: var * 2
ret = lambda var: var * 3
result = 2
result = var1(result)
result = ret(result)
result = var1(result)
print(result)


x = 1
print(++++x)


import random
print(random.seed(3))


mylist=['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
print(mylist[int(-1/2)])


testArr = [11, 22, 33, 22, 11]
result = testArr[0]
for iter in testArr:
 if iter > result:
  result = iter
print(result)


def test1(param):
 return param

def test2(param):
 return param * 2

def test3(param):
 return param + 3

result = test1(test2(test3(1)))
print(result)