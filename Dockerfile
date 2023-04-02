# python 3.9.15 lite
FROM python:3.9.5-slim-buster

WORKDIR /

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["python", "main.py"]