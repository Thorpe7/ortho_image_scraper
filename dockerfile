FROM selenium/standalone-chrome@sha256:4789044942f3102193a0e9b27db94fee9249a2eb51a96cb5bf3477c7092015e9
# selenium/standalone-chrome:nightly

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py

RUN pip install -r /app/requirements.txt 


ENTRYPOINT [ "python main.py" ]