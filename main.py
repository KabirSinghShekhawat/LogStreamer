from sse_starlette.sse import EventSourceResponse
from fastapi import FastAPI, Request
import uvicorn
from app.handlers import log_handler
from app.utils import log_maker

app = FastAPI()


@app.get("/read_logs/{id}")
async def read_logs(id: str, request: Request):
    event = log_handler.read_logs(request)
    return EventSourceResponse(event)


# @app.get("/generate_logs/{lines}")
# async def make_logs(lines: int):
#     await log_maker.run(lines)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="info")
