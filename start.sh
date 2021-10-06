#!/usr/bin/env bash
docker run -d -p 3000:3000 -p 9090:9090 --name isp-grafana-logger moessner/isp-grafana-logger:latest