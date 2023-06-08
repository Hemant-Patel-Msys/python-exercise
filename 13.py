try:
    n1 = int(input("Enter the 1st number: "))
    n2 = int(input("Enter the 2nd number: "))


    if n1 > n2:
        a = n1//n2
        print(a)
    else:
        a = n2 // n1
        print(a)
except ZeroDivisionError:
    print("Zero Devesion error")
except ValueError:
        print("This is not string")
