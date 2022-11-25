from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME = "LogStreamer"
    DEBUG_MODE = True


class ServerSettings(BaseSettings):
    HOST = "127.0.0.1"
    PORT = 8080


class LogMakerSettings(BaseSettings):
    OUT_LOG_FILE_PATH = "app/data/logs.log"
    SEED_FILE_PATH = "app/data/seed.log"
    WRITE_DELAY = 0.5  # s


class LogReaderSettings(BaseSettings):
    READ_DELAY = 0.1  # s
    READ_LOG_FILE_PATH = LogMakerSettings().OUT_LOG_FILE_PATH


class Settings(CommonSettings, ServerSettings, LogMakerSettings, LogReaderSettings):
    pass


settings = Settings()
