l = [56,2,13,1,78,4,6]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[j]>l[i]:
            l[i],l[j] = l[j],l[i]
print(l)
