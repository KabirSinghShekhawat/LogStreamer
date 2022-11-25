from fastapi import Request
import asyncio

STREAM_DELAY = 0.1  # s
RETRY_TIMEOUT = 1500  # ms


async def event_generator(request: Request, log):
    while True:
        # stop sending events if connection has closed.
        if await request.is_disconnected():
            break

        try:
            async for line in log:
                if line:
                    yield {"event": "log_update", "retry": RETRY_TIMEOUT, "data": line}
                    await asyncio.sleep(STREAM_DELAY)
        except asyncio.CancelledError as e:
            print("event cancelled")
            break
