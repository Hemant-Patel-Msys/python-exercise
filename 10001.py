def flatten(l):
    r = []
    for i in l:
        for j in i:
            r.append(j)
    return r


print(flatten([[1, 2], [3, 4]]))