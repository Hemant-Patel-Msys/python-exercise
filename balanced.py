st = input("Enter the choice like this() as you want:- ")
count_1 = 0
#count_2 = 0
for i in st:
    if i == '(':
        count_1 += 1
    if i == ')':
        count_1 -= 1
    if count_1 < 0:
        break

if count_1 >= 1 or count_1 < 0:
    print("InValid")
else:
    print("valid")

