from .. import mod1


def hello():
    print('Hello from subpackage')


def hello_from_parent():
    mod1.hello()
