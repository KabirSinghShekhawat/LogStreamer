from fastapi import Request

from app.config import settings
from app.core.event_generator import event_generator
from app.core.log_reader import LogReader


def stream_logs(request: Request):
    log_file_handle = open(settings.READ_LOG_FILE_PATH)
    log_reader_generator = LogReader(log_file_handle)

    event = event_generator(request, log_reader_generator)
    return event
