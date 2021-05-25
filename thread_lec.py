import time
import threading
import concurrent.futures
import random


def calculation(a, b):
    print(f'calculation started; args: {a}, {b}\n')
    time.sleep(random.randint(2, 5))
    c = a + b
    print(f'calculation finished; result: {c}')
    return c


class Counter:
    def __init__(self, start):
        self.counter = start
        self.increment_lock = threading.Lock()
        self.decrement_lock = threading.Lock()

    def increment(self):
        print('increment started')
        with self.increment_lock:
            print('increment: increment lock acquired')
            with self.decrement_lock:
                print('increment: decrement lock acquired')
                local = self.counter
                local += 1
                time.sleep(random.randint(1, 5))
                self.counter = local
            print('increment: decrement lock released')
        print('increment: increment lock released')
        print('increment finished')

    def decrement(self):
        print('decrement started')
        with self.decrement_lock:
            print('decrement: decrement lock acquired')
            with self.increment_lock:
                print('decrement: increment lock acquired')
                local = self.counter
                local -= 1
                time.sleep(random.randint(1, 5))
                self.counter = local
            print('decrement: increment lock released')
        print('decrement: decrement lock released')
        print('decrement started')

    def show(self):
        return self.counter


if __name__ == '__main__':
    print('application started')
    c = Counter(0)
    print(f'counter: {c.show()}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        print('starting executor')
        executor.map(lambda p: c.increment() if p % 2 == 0 else c.decrement(), range(10))
        print('finished executor')
    print(f'counter: {c.show()}')
    print('application finished')
