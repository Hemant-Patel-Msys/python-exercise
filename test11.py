string = input("Enter the string:- ")
d = {}
for i in string:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

print(d)