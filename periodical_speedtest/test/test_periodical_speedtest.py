from unittest import TestCase
from periodical_speedtest import periodical_speedtest


class TestPeriodicalSpeedtest(TestCase):

    def test_parser(self):
        ping, down, up = periodical_speedtest.parse_isp_performance(['Ping: 10.865 ms', 'Download: 67.06 Mbit/s', 'Upload: 56.72 Mbit/s'])

        self.assertEqual(ping, '10.865')
        self.assertEqual(down, '67.06')
        self.assertEqual(up, '56.72')
