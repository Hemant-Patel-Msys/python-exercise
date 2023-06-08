# Write a program for currency converter without in-built function/method

with open("currency.txt","r") as file:
    lines  = file.readlines()
d = {}
for line in lines:
    parsed = line.split('\t')
    d[parsed[0]] = parsed[1]

amount = int(input("Enter the amount: "))
print("Enter the option as you want to convert currency:- ")
[print(item) for item in d.keys()]
currency = input("Please Enter one of the avilaible option:- ")
print(f"{amount} INR is equal to {amount*float(d[currency])}{currency}")