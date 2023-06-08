def fact(n):
    if n == 1:

        return 1
    else:
        a =  n * fact(n-1)



#print(fact(int(input("Enter the number:-"))))
n = 5
for i in range(2,n+1):
    print(fact(i))
