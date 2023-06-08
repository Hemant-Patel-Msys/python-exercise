#l = [1,2,3,4,5]
l = []
temp = iter(l)

def is_iterator(l1):
    return type(l1) == type(iter(l1))

print(is_iterator(temp))
