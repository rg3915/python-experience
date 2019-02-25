import time
import asyncio

start = time.time()


def tic():
    return 'at %1.1f segundos' % (time.time() - start)


@asyncio.coroutine
def gr1():
    # Demora a ser executada, mas não queremos esperar
    print('gr1 iniciou a execução: {}'.format(tic()))
    yield from asyncio.sleep(2)
    print('gr1 terminou a execução: {}'.format(tic()))


@asyncio.coroutine
def gr2():
    # Demora a ser executada, mas não queremos esperar
    print('gr2 iniciou a execução: {}'.format(tic()))
    yield from asyncio.sleep(2)
    print('gr2 terminou a execução: {}'.format(tic()))


@asyncio.coroutine
def gr3():
    print('Executando enquanto as outras estão bloqueadas: {}'.format(tic()))
    yield from asyncio.sleep(5)
    print('Pronto!')

ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(gr1()),
    ioloop.create_task(gr2()),
    ioloop.create_task(gr3())
]
ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()
