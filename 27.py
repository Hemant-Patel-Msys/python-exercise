import inspect
def test(x1, x2, x3=10):
    pass

argp = inspect.getfullargspec(test)
print(argp.args)

print(argp.defaults)

args_with_default = dict(zip(argp.args[-len(argp.defaults):],argp.defaults))
print(args_with_default)

print(argp.varargs)

print(argp.varkw)

print(argp.annotations)
