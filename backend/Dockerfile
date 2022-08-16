FROM python:3.10.6-slim-buster

COPY . /app
WORKDIR /app
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

RUN apt-get update && apt-get install -y
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install && \
    poetry shell

CMD ["python", "-m", "app"]