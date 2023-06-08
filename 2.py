l = [1,2,3,4,5,6,7,8,1,2,5,8]

unique_list = []
for x in l:
    if x not in unique_list:
        unique_list.append(x)
for x in unique_list:
    print(x,end="")