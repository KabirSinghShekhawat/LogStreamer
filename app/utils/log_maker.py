import os
import asyncio
from random import randint
from app.config import settings

LOG_FILE = settings.OUT_LOG_FILE_PATH
SEED_FILE = settings.SEED_FILE_PATH
DELAY = settings.WRITE_DELAY


async def run(lines=100):
    """
    append a random log line from seed data to logs every second
    """
    with open(LOG_FILE, "w", encoding="utf-8") as log_fh, open(
        SEED_FILE, encoding="utf-8"
    ) as seed_fh:
        seed_fh.seek(os.SEEK_SET, os.SEEK_END)
        SEED_FILE_SIZE = seed_fh.tell()
        seed_fh.seek(os.SEEK_SET)

        while True:
            if lines == 0:
                break

            lines -= 1
            offset = randint(0, SEED_FILE_SIZE)
            seed_fh.seek(offset)  # random byte offset
            """
            readline twice ensures only legible log data is appended to
            the log and not parts of a line.
            """
            seed_fh.readline()
            line = seed_fh.readline()
            log_fh.write(line)

            seed_fh.seek(os.SEEK_SET)
            await asyncio.sleep(DELAY)
