# unlimited positional arguments
def add(*args):
    print(args)
    result = 0
    for n in args:
        result += n
    print(result)


add(5, 2, 1)


# keyword arguments
def calculate(n, **kwargs):
    #print(type(kwargs))
    #print(kwargs["add_n"])
    #for key, value in kwargs.items():
        #print(key)
        #print(value)
    n += kwargs["add_n"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add_n=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        #this way it would require argument to be passed. Get returns None if argument not passed
        #self.make = kwargs["make"]
        #self.model = kwargs["model"]
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make='Nissan', model='GT-R')
print(my_car.model)
