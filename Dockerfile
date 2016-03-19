FROM resin/raspberrypi-python:3.5.1-slim

RUN pip install -e .

CMD ["periodical_speedtest"]
