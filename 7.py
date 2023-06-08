s =  "adfw$vf&yvy*ugv%uy"
l = list(s)
i = 0
j = len(l) - 1

while i < j:
    if not l[i].isalpha():
        i += 1
    elif not l[j].isalpha():
        j -= 1
    else:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
s1 = ''.join(l)
print(s1)