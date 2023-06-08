user = input("Enter the string:- ")
a = len(user)//2
if len(user)%2 != 0:
    b = user[a-1::-1]+user[a]+user[:a:-1]
    print(b)
else:
    b = user[a - 1::-1] + user[:a-1:-1]
    print(b)




