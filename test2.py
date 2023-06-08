unique = []
count  = 0
l = []
str1 = "hemantpatel"
str2 = list(str1)
for i in str2:
    a = (i,count+1)
    if a in str2:
        l.append(a)

    #print(type(a))
    if a not in unique:
        unique.append(a)


for p in unique:
    print(p)