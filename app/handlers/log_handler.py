from fastapi import Request
from app.core.log_reader import LogReader
from app.core.event_generator import event_generator
from app.config import settings


def read_logs(request: Request):
    log_file_handle = open(settings.READ_LOG_FILE_PATH)
    log_reader_generator = LogReader(log_file_handle)
    # log = log_reader_generator.read()

    event = event_generator(request, log_reader_generator)
    return event
