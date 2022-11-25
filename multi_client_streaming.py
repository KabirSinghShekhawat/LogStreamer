from concurrent.futures import ThreadPoolExecutor

from sseclient import SSEClient

stream_url = "http://localhost:8000/stream"


def stream_msg(client_no: int):
    messages = SSEClient(stream_url)

    for msg in messages:
        print(f"{client_no} -> {msg}")

    return f"{client_no} done!"


with ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    for i in range(1, 11):
        future = executor.submit(stream_msg, i)
        futures.append(future)

    for future in futures:
        print(future.result())
