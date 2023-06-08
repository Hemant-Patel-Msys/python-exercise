from typing import Dict, Any

# with the String
unique = []
count  = 0
str1 = "hemantpatel"
str2 = list(str1)
for i in str2:
    a = (i,[x for x in range(len(str1)) if x==str2[x] ])
    if a not in unique:
        unique.append(a)
for x in unique:
    print(x)








