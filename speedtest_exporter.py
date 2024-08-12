# from prometheus_client import start_http_server, Gauge
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import speedtest
import time
import os

IP=os.getenv('PUSH_IP', 'No environment variable set')
PUSHGATEWAY = 'http://' + IP + ':9091'
JOB_NAME = 'internet_speed_test'

def run_speed_test():
    s = speedtest.Speedtest(secure=True)
    s.get_best_server()
    download_speed = s.download()
    upload_speed = s.upload()
    ping = s.results.ping
    return download_speed, upload_speed, ping

def push_metrics(download, upload, ping):
    registry = CollectorRegistry()
    download_gauge = Gauge('speedtest_download_speed', 'Download speed in Mbps', registry=registry)
    upload_gauge = Gauge('speedtest_upload_speed', 'Upload speed in Mbps', registry=registry)
    ping_gauge = Gauge('speedtest_ping', 'Ping in milliseconds', registry=registry)
    download_gauge.set(download)
    upload_gauge.set(upload)
    ping_gauge.set(ping)
    push_to_gateway(PUSHGATEWAY, job=JOB_NAME, registry=registry)

def main():
    while True:
        try:
            download_speed, upload_speed, ping = run_speed_test()
            print(f"Download: {download_speed} Mbps, Upload: {upload_speed} Mbps, Ping: {ping} ms")
            push_metrics(download_speed, upload_speed, ping)
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(15)

if __name__ == '__main__':
    main()