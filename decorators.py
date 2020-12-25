import functools

def logger(name):
    def simple_logger(func):
        @functools.wraps(func)
        def result(*args, **kwargs):
            print(name + ": " + func.__name__ + " is called")
            val = func(*args, **kwargs)
            print(name + ": " + func.__name__ + ' is finished')
            return val

        return result

    return simple_logger

class Statistics:
    def __init__(self, name):
        self.name = name
        self.counter = 0

    def __call__(self, f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            self.counter += 1
            print(self.name + ": function " + f.__name__ + " is called " + str(self.counter) + " times")
            return f(*args, **kwargs)
        return wrapper

