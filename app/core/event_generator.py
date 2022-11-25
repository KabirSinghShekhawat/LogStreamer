from fastapi import Request
import asyncio

STREAM_DELAY = 0.1  # s
RETRY_TIMEOUT = 1500  # ms


async def event_generator(request: Request, log_generator):
    while True:
        # stop sending events if connection has closed.
        if await request.is_disconnected():
            break

        try:
            async for line in log_generator.read():
                line_val = await line
                if line_val:
                    print(line_val)
                    yield {"event": "log_update", "retry": RETRY_TIMEOUT, "data": line_val}

                else:
                    await asyncio.sleep(STREAM_DELAY)

        except asyncio.CancelledError as e:
            print("event cancelled")
            break
