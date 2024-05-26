FROM python:3.9-slim

RUN pip install speedtest-cli prometheus_client --progress-bar off

COPY speedtest_exporter.py /speedtest_exporter.py

CMD ["python", "/speedtest_exporter.py"]
