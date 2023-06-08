import math

s = 0
for i in range(1,10000):
    s = s+i
    #print(s)
    s1 = math.sqrt(s)
    if s1.is_integer():
        print(i)


n=10000
c=1
for i in range(n+1):
    sum=(i*(i+1))//2
    if sum==c**2:
        print(i)
    elif sum>c**2:
        c+=1