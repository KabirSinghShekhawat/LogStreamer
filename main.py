import time
import os

class LogStreamer:
    def __init__(self, file_handle) -> None:
        self.file_handle = file_handle

    def read(self):
        self.file_handle.seek(os.SEEK_SET, os.SEEK_END) # goto EOF
        while True:
            line = self.file_handle.readline()
            if not line:
                time.sleep(0.5) # wait for new logs
                continue
            yield line



log_file = open("logs.log", "r")

log_streamer = LogStreamer(log_file)

for line in log_streamer.read():
    print(line)
