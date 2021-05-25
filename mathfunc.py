import click

def add(a, b):
    return a + b


def mult(a, b):
    return a * b


def div(a, b):
    if a == 0 and b == 0:
        return 0
    return a/b


def degree(a, b):
    if type(b) == float:
        raise ValueError("float degree")
    result = 1
    if b < 0:
        for i in range(-b):
             result = result / a
    else:
        for i in range(b):
            result = result * a
    return result

def calc(a,b,c):
    sum = 0
    for x in range(a):
        sum = add(sum, a)
    d = int(div(sum, b))
    return degree(c, d)

@click.group()
def grp():
    pass


@grp.command()
@click.option("--repeats", default=1, help="number of repeats")
@click.argument("value")
def action(repeats, value):
    l = [int(value), int(value)]
    for i in range(repeats):
        print("Begin {} repeat".format(i))
        v1, v2 = l[-2], l[-1]
        l.append(v1 + v2)
        print("End of {} repeat, current value: {}".format(i, l[-1]))


if __name__ == "__main__":
    grp()
