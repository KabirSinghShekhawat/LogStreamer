import uvicorn
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse

from config import settings
from handlers import log_handler

app = FastAPI()


@app.get("/stream")
async def stream(request: Request):
    event = log_handler.stream_logs(request)
    return EventSourceResponse(event)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG_MODE,
        log_level="info"
    )
