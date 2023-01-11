FROM python:3.10.6-slim-buster

COPY . /dir
WORKDIR /dir
# ENV PYTHONPATH=/dir
# ENV PYTHONUNBUFFERED=1

# EXPOSE 8000

RUN pip install -r requirements.txt
# RUN apt-get update && apt-get install -y
# RUN pip install --upgrade pip && \
#     pip install poetry && \
#     poetry config experimental.new-installer false && \
#     poetry config virtualenvs.create false && \
#     poetry install && \
#     poetry shell

CMD ["python", "-m", "app"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]