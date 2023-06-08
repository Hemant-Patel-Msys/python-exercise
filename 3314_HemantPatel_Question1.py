l1 = ['siya','priya','jiya']
l2 = [170,120,130]
for i in range(len(l2)):
    for j in range(i,len(l2)):
        if l2[i]>l2[j]:
            l1[i],l1[j] = l1[j],l1[i]
            l2[i],l2[j] = l2[j],l2[i]

print(l1)
print(l2)