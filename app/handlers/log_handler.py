from fastapi import Request

from config import settings
from core.event_generator import event_generator
from core.log_reader import LogReader


def stream_logs(request: Request):
    log_file_handle = open(settings.READ_LOG_FILE_PATH)
    log_reader_generator = LogReader(log_file_handle)

    event = event_generator(request, log_reader_generator)
    return event
