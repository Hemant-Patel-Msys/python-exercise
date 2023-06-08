a=[['n','i','k'],['a','b','c'],['d','e','f']]
#nbf,icd,kae
i = 0
j = 1
k = 2
count = 0
while count > 4:
    print(a[0][i],a[1][j],a[2][k])
    i += 1
    j += 1
    k += 1
    if i > 2:
        i = 0
    elif j > 2:
        j = 0
    elif k > 2:
        k = 0
    count += 1