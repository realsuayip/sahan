FROM python:3.11.2-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add netcat-openbsd
RUN python -m pip install pip-tools==6.12.3

WORKDIR /code

ADD ./requirements.txt /code/requirements.txt
RUN pip-sync requirements.txt --pip-args "--no-cache-dir --no-deps"

COPY . /code
ENTRYPOINT ["/code/entrypoint.sh"]
