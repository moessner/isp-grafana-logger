FROM grafana/grafana:latest
ADD . /
CMD [ "python3", "install", "-r", "./requirements.txt"]
CMD [ "python3", "./logging.py" ]
