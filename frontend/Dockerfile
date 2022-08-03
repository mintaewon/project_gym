FROM python:3.10.6-slim-buster

COPY . /app
WORKDIR /app
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    poetry shell

CMD ["streamlit", "run", "front.py"]
