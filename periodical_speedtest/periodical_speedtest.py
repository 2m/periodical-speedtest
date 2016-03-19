from io import StringIO
from speedtest_cli import speedtest
import argparse
import os
import requests
import schedule
import sys
import time


# humbly taken from http://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


class Argv():
    def __init__(self, argv):
        self.argv = argv

    def __enter__(self):
        self._argv = sys.argv
        sys.argv = self.argv

    def __exit__(self, *args):
        sys.argv = self._argv


def run_speedtest():
    with Capturing() as output, Argv(['speedtest-cli', '--simple']):
        speedtest()
    return output


def parse_isp_performance(speed_test_results):
    ping = speed_test_results[0].split(' ')[1]
    download = speed_test_results[1].split(' ')[1]
    upload = speed_test_results[2].split(' ')[1]

    return (ping, download, upload)


def measure_and_upload(args):
    ping, download, upload = parse_isp_performance(run_speedtest())

    r = requests.post('https://maker.ifttt.com/trigger/{}/with/key/{}'.format(args.maker_event, args.maker_key), json={'value1': ping, 'value2': download, 'value3': upload})
    print(r.text)


def main():

    parser = argparse.ArgumentParser('periodical_speedtest')
    parser.add_argument('--interval-minutes', dest='interval_minutes', default=os.getenv('INTERVAL_MINUTES', '15'), type=int, help='Speed check interval in minutes')
    parser.add_argument('--maker-event', dest='maker_event', default=os.getenv('MAKER_EVENT', 'isp_performance_measured'), help='Maker channel event name')
    parser.add_argument('--maker-key', dest='maker_key', default=os.getenv('MAKER_KEY', None), help='Maker channel key')
    args = parser.parse_args()

    if not args.maker_key:
        print('Please set Maker Channel Key by adding --maker-key CLI option or setting MAKER_KEY environment variable.')
        sys.exit()

    print('Will run speedtest every {} minutes.'.format(args.interval_minutes))

    schedule.every(args.interval_minutes).minutes.do(measure_and_upload, args)

    while True:
        schedule.run_pending()
        time.sleep(1)
