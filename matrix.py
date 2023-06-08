m = [[1, 2, 3], [4, 5, 6], [1, 8, 9]]
a = []
b = []
for i in range(len(m)):
    for j in range(len(m)):
        if i == j:
            a.append(m[i][j])
    b.append(m[i][(len(m) - 1) - i])

print(abs(sum(a) - sum(b)))