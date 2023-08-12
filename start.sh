docker run -d --name=promtheus -p 9090:9090 -v $PWD/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus

docker run -d --name=grafana -p 3000:3000 grafana/grafana

/usr/local/bin/python3 metrics_exposer.py 18001 &
/usr/local/bin/python3 metrics_exposer.py 18002 &
