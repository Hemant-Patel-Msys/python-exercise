def rangoli(n,width):
    c=n
    str=""
    for j in range(width):
        if j<(width//2) and j%2==0:
            str+=chr(96+c)
            c-=1
        elif j<(width//2) and j%2==1:
            str+="-"
        elif j==(width//2) and j%2==0:
            str+=chr(96+c)
        elif j>(width//2) and j%2==0:
            c+=1
            str+=chr(96+c)
        elif j>(width//2) and j%2==1:
            str+="-"
    return str



n=5
width=4*n-3
for i in range(1,width+1,4):
    if i==1:
        str=chr(96+n)
    else:
        str=rangoli(n,i)
    print((str).center(width," "))

for i in  range(width-4,0,-4):
    if i==1:
        str=chr(96+n)
    else:
        str=rangoli(n,i)
    print((str).center(width," "))