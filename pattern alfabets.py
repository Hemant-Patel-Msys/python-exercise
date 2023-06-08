n = 8

for i in range(n):
    for j in range(n):

        if i == 0 or j == 0 or j == n-1 or i == n-1:
            print('*',end='&')
        else:
            print('$',end='!')
        if i ==0 or j == 1 or j == n-5 or i == n-5 or  j == n-3 or i == n-3 or  j == n-7 or i == n-7 or j == n-1:
            print('@',end='%')
        else:
            print('#',end='^')
    print()