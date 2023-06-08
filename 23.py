def highest_sum(st:str):
    temp = 0
    st = set(st)
    for i in st:
        temp += int(i)
    new_st = str(temp)
    set_list = list(new_st)
    if set_list == list(set(set_list)):
        return new_st
    else :
        return highest_sum(new_st)

obj = highest_sum("1211")
print(obj)