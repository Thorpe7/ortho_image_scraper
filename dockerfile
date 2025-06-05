FROM python@sha256:afc139a0a640942491ec481ad8dda10f2c5b753f5c969393b12480155fe15a63
# python:3.12.3-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY . /app/

RUN pip install -r /app/requirements.txt

CMD [ "python", "main.py" ]