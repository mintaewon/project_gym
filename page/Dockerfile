FROM python:3.10.6-slim-buster

COPY . /dir
WORKDIR /dir

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pymysql

CMD ["python", "-m", "app"]