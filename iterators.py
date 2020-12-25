class MyIterable:
    def __init__(self, l):
        self.l = l

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.l):
            raise StopIteration
        self.index += 1
        return self.l[self.index - 1]

    def __len__(self):
        return len(self.l)

    def __getitem__(self, item):
        return self.l[item]


class MyGenerator:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.num
        self.num += 1
        return value


def infinite_gen():
    num = 0
    while True:
        yield num
        num += 1

def two_value():
    print('Initialization')
    yield 'First value'
    print('Preparing second value')
    yield 'Second value'
    print('Finished')