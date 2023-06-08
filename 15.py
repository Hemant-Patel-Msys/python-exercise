lst = ['data','science','artificial', 'intelligence']
dct = {'data': 5, 'science': 3, 'machine':1, 'learning': 8}

new_dict = {}
for item in lst:
    if item in dct:
        new_dict[item] = dct[item]
    else:
        new_dict[item] = len(item)
print(new_dict)
