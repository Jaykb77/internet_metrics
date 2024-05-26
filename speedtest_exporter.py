from prometheus_client import start_http_server, Gauge
import speedtest
import time

def run_speedtest():
    s = speedtest.Speedtest(secure=True)
    s.download()
    s.upload()
    return s.results.dict()

def collect_speedtest_data():
    results = run_speedtest()
    download_speed.set(results['download'])
    upload_speed.set(results['upload'])
    ping.set(results['ping'])

if __name__ == "__main__":
    download_speed = Gauge('speedtest_download_speed', 'Download speed')
    upload_speed = Gauge('speedtest_upload_speed', 'Upload speed')
    ping = Gauge('speedtest_ping', 'Ping')

    start_http_server(9100)
    while True:
        collect_speedtest_data()
        time.sleep(30)  # Run every 30 seconds