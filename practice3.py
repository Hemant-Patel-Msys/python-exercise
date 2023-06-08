a = [1,2,3,4,5,6,2,3,4,5]
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
if d.values==1:
    print(d.keys)