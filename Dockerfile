FROM python:3.10.6-slim

ENV DIRPATH=/LogStreamer
WORKDIR $DIRPATH

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY /app ./app/
COPY client.sh multi_client_streaming.py ./

EXPOSE 8080

CMD [ "python", "app/main.py" ]
