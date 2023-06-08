import threading


def hello(n):
    print("Hello" * n)


t = threading.Thread(target=hello, args=(5,))
t.start()
print(t)