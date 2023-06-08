input_1 = int(input())
l = [input() for x in range(input_1)]
def decor(fn):
    def inner(l):
        fn("+91"+" "+c[-10:5]+" "+c[-5:] for c in l)
    return inner

@decor
def sorted_l(l):
    print(*sorted(l),sep='\n')

sorted_l(l)