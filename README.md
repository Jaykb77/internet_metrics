# internet_metrics
Docker compose to setup internet speed exporter with prometheus and grafana to monitor and visualize

# requirements
docker  
docker-compose

# STEP 1. build exporter
cd to cloned directory, thenrun below command to build speedtest-exporter image and bring up all containers
```
docker build -t speedtest-exporter . && docker-compose up -d
```

# STEP 2. access grafana dashboard in browser
Access http://localhost:3000.  
Initial user password admin/admin  
Check internet-speed dashboard in grafana  
Prometheus instance will be available at:
http://localhost:9090/

# STEP 3. stop containers
```
docker-compose down
```

# How it looks

![internet speed dashboard](files/internet_metrics_screenshot.jpg)

# Disclaimer
The metrics are collected using speedtest-cli. All metrics are not entirely reliable as per the details in:
https://github.com/sivel/speedtest-cli
