import logging
import os
import asyncio
import time
from random import randint
from app.config import settings

LOG_FILE = settings.OUT_LOG_FILE_PATH
SEED_FILE = settings.SEED_FILE_PATH
DELAY = settings.WRITE_DELAY


def run(lines=100):
    """
    append a random log line from seed data to logs every second
    """
    logger = logging.getLogger("log-stream")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(LOG_FILE)
    logger.addHandler(fh)

    with open(SEED_FILE, encoding="utf-8") as seed_fh:
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
            logger.info(line.strip("\n"))

            seed_fh.seek(os.SEEK_SET)
            # await asyncio.sleep(DELAY)
            time.sleep(DELAY)


if __name__ == "__main__":
    run(100)