a = [8,9,10,"f",5,8,"d"]
res = []

for i in a:
    if isinstance(i,int):
        res.append(i*i)
    elif isinstance(i,str):
        res.append(i*2)
print(res)
