#!/usr/bin/env bash
docker image rm moessner/isp-grafana-logger:latest
docker build -t moessner/isp-grafana-logger:latest .