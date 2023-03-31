# python 3.9.15 lite
FROM python:3.9.5-slim-buster

WORKDIR /app

COPY requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . /app

EXPOSE 3000

CMD ["python", "app.py"]