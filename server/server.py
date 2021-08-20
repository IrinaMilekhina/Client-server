import asyncio
import os

server_id = os.environ.get('ID')

port = 15555


async def respond(writer, time):
    await asyncio.sleep(time)
    writer.write(f'{server_id}-{time}'.encode())
    await writer.drain()


async def handle_echo(reader, writer):
    while True:
        data = await reader.read(100)
        if not data:
            break
        s = data.decode()
        asyncio.create_task(respond(writer, int(s)))
    writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, '0.0.0.0', port)

    async with server:
        await server.serve_forever()


asyncio.run(main())
