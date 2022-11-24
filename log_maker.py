import os
import time
from random import randint


def run():
    """
        append a random log line from seed data to logs every second
    """
    with open("logs.log", "w", encoding="utf-8") as log_fh, open("seed.log", encoding="utf-8") as seed_fh:
        seed_fh.seek(0, os.SEEK_END)
        SEED_FILE_SIZE = seed_fh.tell()
        seed_fh.seek(0)

        while True:
            offset = randint(0, SEED_FILE_SIZE)
            seed_fh.seek(offset)  # random byte offset
            '''
            readline twice ensure only legible log data is appended to
            the log and not parts of a line.
            '''
            seed_fh.readline()
            line = seed_fh.readline()
            log_fh.write(line)

            seed_fh.seek(0)
            time.sleep(0.1)


if __name__ == "__main__":
    run()
