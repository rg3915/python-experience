import asyncio


@asyncio.coroutine
def empacotar_bala():
    print('Empacotando balas...')

    # parada para verificar se tem cliente no balcão
    yield from asyncio.sleep(0)

    # troca de contexto
    print('Explicitamente voltando a empacotar balas.')


@asyncio.coroutine
def atender_balcao():
    print('Explicitamente verificando se tem cliente no balcão...')

    yield from asyncio.sleep(0)

    print('Voltando a empacotar as balas.')


ioloop = asyncio.get_event_loop()  # Event loop

tasks = [
    ioloop.create_task(empacotar_bala()),
    ioloop.create_task(atender_balcao())
]

wait_tasks = asyncio.wait(tasks)

ioloop.run_until_complete(wait_tasks)

ioloop.close()
