string = "Nittin and his mom went to park last friday " \
        "Nittin's mom observed that the weather was too cool " \
        "If we reverse the number 1331 then we also we get 1331"
string = string.lower()
counter = 0
for i in string.split():
    if len(i) == 1:
        continue

    elif i == i[::-1]:
        counter += 1
print(counter)









