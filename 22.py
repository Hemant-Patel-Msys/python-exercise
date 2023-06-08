n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(i,n-1+1):
        print(end=" ")

    for j in range(i,0,-1):
        print("_",end="")
    for j in range(2,0,i):
        print("",end="")
    print("*")


n = 5

for i in range(1,n+1):
    for j in range(i,n-1+1):
        print(end=" ")
    for j in range(i,0,-1):
        print(i,end="")
    for j in range(2,i):
        print(i,end="")
    print()



