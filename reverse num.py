n = int(input(("Enter the number: ")))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum = sum*10 + digit
    temp = temp // 10

print(sum)