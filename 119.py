'''19. Write a program using decorators to print the traffic signal messages
Expected output -
RED : STOP
YELLOW : SLOW DOWN
GREEN : GO
The decorator should be working in this order'''


# defining a decorator
def hello_decorator(func):

    def inner1():
        print("RED:STOP")

        func()

        print("GREEN:GO")

    return inner1

def function_to_be_used():
    print("YELLOW:SLOW DOWN")

a = hello_decorator(function_to_be_used)

a()