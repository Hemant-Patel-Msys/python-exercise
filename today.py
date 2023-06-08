s = "hemantpatel"
l = []
count = 0
for i in s:
    for j in range(len(s)):
        if s[j] == i:
           # print(i)
            l.append(i)

for i in l:
    print(i,count + 1)







