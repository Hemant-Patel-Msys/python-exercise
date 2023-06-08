import multiprocessing
import math
import threading




def squrt(num):
     print(math.sqrt(num))


def cube(num):
    print(num ** 3)


def square(num):
    print(num ** 2)

t1 = threading.Thread(target=squrt,args=(5000000,))
t2 = threading.Thread(target=cube,args=(5000000,))
t3 = threading.Thread(target=square,args=(5000000,))

t1.start()
t2.start()
t3.start()
print(t1)
print(t2)
print(t3)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square, args=(5000000,))
    p2 = multiprocessing.Process(target=cube, args=(5000000,))
    p3 = multiprocessing.Process(target=squrt,args=(5000000,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("Done!")


