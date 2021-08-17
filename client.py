from socket import socket, AF_INET, SOCK_STREAM
import random
import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

while True:
    n = str(random.randint(0, 10))
    asyncio.run(tcp_echo_client(n))


# while True:
#     s = socket(AF_INET, SOCK_STREAM)
#     s.connect(('localhost', 8888))
#     msg = str(random.randint(0, 10))
#     s.send(msg.encode('utf-8'))
#     print(f'отправлено на сервер: {msg}')
#     data = s.recv(4096)
#     print(data.decode('utf-8'))
#     s.close()


# async def sending():
#     await asyncio.sleep(random.randint(0, 10))
#     msg = str(random.randint(0, 10))
#     s.send(msg.encode('utf-8'))
#     print(f'отправлено на сервер: {msg}')
#
#
# while True:
#     ioloop = asyncio.get_event_loop()
#     tasks = [ioloop.create_task(sending())]
#     wait_tasks = asyncio.wait(tasks)
#     ioloop.run_until_complete(wait_tasks)
#
#     ioloop.close()
#     data = s.recv(4096)
#     print(data.decode('utf-8'))
#     s.close()
