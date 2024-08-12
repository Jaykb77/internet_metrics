#build with docker build -t speedtest-exporter .

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt speedtest_exporter.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "speedtest_exporter.py"]