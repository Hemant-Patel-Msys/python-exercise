def float_range(start,stop,step):
    while start < stop:
        yield start
        start += step

start = 0.5
stop = 2.5
step = 0.5

a = float_range(start,stop,step)
a = list(a)
for i in a:
    print(i)

