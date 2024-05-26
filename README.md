# internet_metrics
Docker compose to setup internet speed exporter with prometheus and grafana to monitor and visualize

# STEP 1. build exporter
docker build -t speedtest-exporter .

# STEP 2. bring up containers
docker-compose up -d

# STEP 3. access grafana dashboard in browser
Initial user password admin/admin
Check internet-speed dashboard in grafana
