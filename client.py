import asyncio
import random
import yaml

times = 10

with open('conf.yml') as f:
    conf_data = yaml.safe_load(f)
ports = list(conf_data.values())


async def receive(reader):
    for i in range(times):
        data = await reader.read(100)
        print(data.decode())


async def send(writer):
    for i in range(times):
        interval = random.randint(1, 10)
        s = str(random.randint(1, 10))
        writer.write(s.encode())
        await asyncio.sleep(interval)


async def client(port):
    reader, writer = await asyncio.open_connection('127.0.0.1', port)

    await asyncio.gather(
        asyncio.create_task(receive(reader)),
        asyncio.create_task(send(writer))
    )
    writer.close()


async def gen_connections():
    await asyncio.gather(*[asyncio.create_task(client(port)) for port in ports])


asyncio.run(gen_connections())
