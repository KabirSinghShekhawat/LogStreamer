import asyncio

from fastapi import Request

STREAM_DELAY = 0.1  # s


async def event_generator(request: Request, log_generator):
    while True:
        # stop sending events if connection has closed.
        if await request.is_disconnected():
            break

        try:
            async for line in log_generator.read():
                if line:
                    yield {"event": "log_update", "data": line}
                else:
                    await asyncio.sleep(STREAM_DELAY)

        except asyncio.CancelledError as _:
            print("event cancelled")
            break
