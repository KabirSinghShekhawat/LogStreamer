import logging
import os
import sys
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
        seed_file_size = seed_fh.tell()
        seed_fh.seek(os.SEEK_SET)

        while True:
            if lines == 0:
                break

            lines -= 1
            offset = randint(0, seed_file_size)
            seed_fh.seek(offset)  # random byte offset
            """
            readline twice ensures only legible log data is appended to
            the log and not parts of a line.
            """
            seed_fh.readline()
            line = seed_fh.readline()
            line = line.strip("\n")

            logger.info(line)
            print("log: " + line + "\n")

            seed_fh.seek(os.SEEK_SET)
            time.sleep(DELAY)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        run()
    else:
        num_lines = sys.argv[1]
        run(int(num_lines))
