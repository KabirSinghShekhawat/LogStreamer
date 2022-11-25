from sse_starlette.sse import EventSourceResponse
from fastapi import FastAPI, Request
import uvicorn
from app.handlers import log_handler

app = FastAPI()


@app.get("/stream")
async def read_logs(request: Request):
    event = log_handler.read_logs(request)
    return EventSourceResponse(event)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="info")
