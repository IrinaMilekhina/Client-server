from socket import socket, AF_INET, SOCK_STREAM
import time
import asyncio

serv_id = 1234
s = socket(AF_INET, SOCK_STREAM)
# принимает коннект с любого айпи по порту 8888
s.bind(('', 8888))
# сколько клиентов мы будем слушать
s.listen(5)


async def working_on_n():
    # принимаем пакет от клиента, указываем размер пакета в байтах
    data = client.recv(4096)
    n = int(data.decode('utf-8'))
    print(f'получен пакет {n}')
    await asyncio.sleep(n)
    # передаем, строку нужно преобразовать в байты
    msg = f'{serv_id}-{n}'
    client.send(msg.encode('utf-8'))
    print(f'отправлен пакет {n}')


async def asynchronous():
    tasks = [asyncio.ensure_future(working_on_n())]
    await asyncio.wait(tasks)

while True:
    # принимаем клиент и адрес от socket.accept()
    client, addr = s.accept()
    asyncio.run(asynchronous())
    client.close()
