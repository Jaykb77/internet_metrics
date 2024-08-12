#build with docker build -t speedtest-exporter --build-arg PUSH_IP=<IP> .

FROM python:3.9-slim

ARG PUSH_IP

WORKDIR /app

COPY requirements.txt speedtest_exporter.py .

RUN pip install --no-cache-dir -r requirements.txt && sed -i 's/push_gateway_ip/'"${PUSH_IP}"'/' ./speedtest_exporter.py

CMD ["python", "speedtest_exporter.py"]