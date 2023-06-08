string = "My name is hemant"
string = string.split()
max = 0
for i in string:
    if len(i) > max:
        max = len(i)
print(string)
newstring = ""
count = 0

while count < max:

    for i in string:
        if count >= len(i):
            continue
        else:
            newstring += i[count]
    newstring += " "
    count += 1
print(newstring)