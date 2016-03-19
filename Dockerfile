FROM resin/raspberrypi-python:3.5.1-slim

COPY . /app

WORKDIR /app

RUN pip install .

CMD ["periodical_speedtest"]
