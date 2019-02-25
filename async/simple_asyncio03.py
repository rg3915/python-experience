import random
from time import sleep
import asyncio


def task(pid):
    """Uma tarefa não deterministica"""
    sleep(random.randint(0, 2) * 0.001)
    print('Task %s terminada' % pid)


@asyncio.coroutine
def task_coro(pid):
    """Uma tarefa deterministica"""
    yield from asyncio.sleep(random.randint(0, 2) * 0.001)
    print('Task %s terminada' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


@asyncio.coroutine
def asynchronous():
    tasks = [asyncio.async(task_coro(i)) for i in range(1, 10)]
    yield from asyncio.wait(tasks)


print('Síncronamente:')
synchronous()

ioloop = asyncio.get_event_loop()
print('Assíncronamente:')
ioloop.run_until_complete(asynchronous())

ioloop.close()
