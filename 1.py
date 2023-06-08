l = [11,6,8,9,5,4,6,7,4,6]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[j]>l[i]:
            l[i],l[j] = l[j],l[i]
print(l[1])
