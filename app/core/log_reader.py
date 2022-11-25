import asyncio
import os


class LogReader:
    DELAY = 0.1  # s

    def __init__(self, file_handle) -> None:
        self.file_handle = file_handle

    async def read(self):
        self.file_handle.seek(os.SEEK_SET, os.SEEK_END)  # goto EOF

        while True:
            line = self.file_handle.readline()
            if not line:
                await asyncio.sleep(LogReader.DELAY)  # wait for new logs
                continue
            yield line
