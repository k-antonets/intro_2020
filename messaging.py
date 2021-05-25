import time
import multiprocessing
import concurrent.futures
import random
import logging
import queue


def writer(messenger:  queue.Queue, event: threading.Event, id: str):
    while not event.is_set():
        message = random.randint(1, 200)
        messenger.put(f'{id}:{message}')
        logging.info(f'Writer {id} writes message {message}')


def reader(messenger: queue.Queue, event: threading.Event, id: str):
    result = []
    while not event.is_set() or not messenger.empty():
        message = messenger.get()
        result.append(f'Reader {id} reads message {message}')
    return result


def factorial(n):
    result = 1
    for i in range(n):
        time.sleep(1)
        result *= i + 1
    return result


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

    q = queue.Queue(maxsize=15)
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
        results = executor.map(factorial, range(10))
        for r in results:
            print(r)
    print(f'time spent: {time.perf_counter() - start}')

    p = multiprocessing.Process(target=)
    p.run()


class TreeNode:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None