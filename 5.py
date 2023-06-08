l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30,17]
prime=[]
for i in l1:
    flag = 0

    if i==0 or i==1:
        pass
    elif i==2:
        prime+=[i**2]
    else:
        for j in range(2,i):
            if i%j==0:
                flag+=1
        if flag>=1:
            pass
        else:
            prime+=[i**2]
print(prime)