
a=  open("one.txt", "r")
s=""
line= a.readlines()
sum=0
for i in line:
    for j in i:
        if j.isdigit():
            s+=j
    s+=" "
for i in s.split():
    sum=sum+ int(i)
print(sum)