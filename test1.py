

# String
unique = []
str1 = input("Enter the string:- ")
for i in str1:
    a = (i,len([ x for x in range(len(str1)) if str1[x] == i]))
    if a not in unique:
        unique.append(a)
for x in unique:
    print(x)


