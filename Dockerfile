FROM resin/raspberrypi-python:3.5.1-slim

COPY . /app

WORKDIR /app

RUN pip install -e .

CMD ["periodical_speedtest"]
