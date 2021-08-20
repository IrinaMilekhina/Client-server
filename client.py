import asyncio
import random
import yaml

with open('conf.yml') as f:
    conf_data = yaml.safe_load(f)
ports = list(conf_data.values())


async def receive(reader, times):
    for i in range(times):
        data = await reader.read(100)
        print(data.decode())


async def send(writer, times, port):
    for i in range(times):
        interval = random.randint(1, 10)
        s = str(random.randint(1, 10))
        print(f'Sent: {s} to {port}')
        writer.write(s.encode())
        await asyncio.sleep(interval)


async def client(port):
    reader, writer = await asyncio.open_connection('127.0.0.1', port)

    await asyncio.gather(
        asyncio.create_task(receive(reader, 10)),
        asyncio.create_task(send(writer, 10, port))
    )
    writer.close()


async def gen_connections():
    await asyncio.gather(*[asyncio.create_task(client(port)) for port in ports])


asyncio.run(gen_connections())
