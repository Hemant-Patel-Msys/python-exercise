with open("file.txt","r") as file:
    lines = file.readlines()

lines.reverse()

for line in lines:
    print(line)

