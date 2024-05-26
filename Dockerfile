FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY speedtest_exporter.py .

CMD ["python", "speedtest_exporter.py"]