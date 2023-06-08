st = input("Enter the choice like this() as you want:- ")
count_1 = 0
count_2 = 0
if st == st[::-1]:
    for i in st:
        if i.startswith('('):
            count_1 += 1
        if i.startswith(')'):
            count_2 += 1
    if count_1 == count_2:
        print("Balanced")
else:
    print("unbalanced")


