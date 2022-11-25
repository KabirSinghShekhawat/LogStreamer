FROM python:3.10.6-slim

ENV DIRPATH=/app/LogStreamer
WORKDIR $DIRPATH

COPY ./requirements.txt $DIRPATH/requirements.txt

RUN pip install --no-cache-dir --upgrade -r $DIRPATH/requirements.txt

COPY /app $DIRPATH/
COPY client.sh multi_client_streaming.py main.py $DIRPATH/

EXPOSE 8000

CMD [ "python", "main.py" ]
