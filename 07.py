# 7. Write a program using dictionary comprehension which will contain the key value pair of i:i**2.
# Value of ‘i’ will start from 1 and will go upto 10.


myDict = {x: x**2 for x in range(1,11)}
print(myDict)