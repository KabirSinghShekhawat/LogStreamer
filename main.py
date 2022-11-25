import uvicorn
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse

from app.handlers import log_handler

app = FastAPI()


@app.get("/stream")
async def stream(request: Request):
    event = log_handler.stream_logs(request)
    return EventSourceResponse(event)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="info")
