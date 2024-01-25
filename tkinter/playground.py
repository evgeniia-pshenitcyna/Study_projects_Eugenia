# unlimited positional arguments
def add(*args):
    result = 0
    for n in args:
        result += n
    print(result)


add(5, 2, 1)


# keyword arguments
def calculate(**kwargs):
    print(type(kwargs))


calculate(add_n=3, multiply=5)
