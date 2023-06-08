try:
    n = int(input("Enter the int:- "))
    a = int(input("Enter the int:- "))
    print(n//a)
except ValueError:
    print("Please provide correct input")