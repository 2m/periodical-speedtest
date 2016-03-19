from setuptools import setup, find_packages
from periodical_speedtest import __version__


setup(
    name='periodical-speedtest',
    version=__version__,
    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'periodical-speedtest = periodical_speedtest.periodical_speedtest:main',
        ],
    },

    install_requires=[
        'speedtest-cli==0.3.4',
        'schedule==0.3.2',
        'requests==2.9.1',
    ],
    setup_requires=['tox-setuptools'],
    tests_require=['tox'],
    test_suite='periodical_speedtest.test',

    license='Apache 2',
    description='Periodical ISP performance test',
    url='https://github.com/samanos/periodical-speedtest',
)
