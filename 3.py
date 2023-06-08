l = [2, 50, 78, 67, 98, 65]


user = int(input("Enter the choice what item you want to delete:- "))

for i in range(len(l)):
    index = i
    if user == index:
        l.pop(user)

print(l)
