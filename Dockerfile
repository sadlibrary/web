FROM python:3.10

WORKDIR /app/

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY web/ ./
COPY entrypoint.sh ./

RUN ["chmod", "+x", "./entrypoint.sh"]

CMD ./entrypoint.sh