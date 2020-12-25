def add(a, b):
    return a + b


def dirty_add(a, b):
    result = a + b
    print(result)
    return result


def clean_append(arr, val):
    return [*arr, val]


def sum(*vals):
    result = 0
    for i in vals:
        result += i
    return i


def print_dict(**kwargs):
    for k in kwargs:
        print(k + ": " + str(kwargs[k]))


def process_list(l, operation):
    result = []
    for i in l:
        result.append(operation(i))
    return result


def create_multiplier(n):
    m = n * 2
    def mult(i):
        return i * m
    return mult


def mult_by_2(i):
    return i*2

def infinit(start):
    a = [start]
    def next():
        result = a[0]
        a[0] = result + 1
        return result

    return next

def func(x):
    return x*2

"""
[1,2,3,4]
1: prev = 0, next = 1 => 1
2: prev = 1, next = 2 => 3
3: prev = 3, next = 3 => 6
4: prev = 6, next = 4 => 10

"""