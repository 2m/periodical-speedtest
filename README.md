Periodical ISP performance test
===============================

This is a periodical ISP performance test inspired by an [article in Makezine](http://makezine.com/projects/send-ticket-isp-when-your-internet-drops/). When installed, this python project provides `periodical-speedtest` executable which accepts the following command line options or environment variables:

* `--maker-key` CLI option or `MAKER_KEY` environment variable, required. Key for your [Maker Channel](https://ifttt.com/maker).
* `--interval-minutes` CLI option or `INTERVAL_MINUTES`. Defaults to 15 minutes and controls the interval between tests.
* `--maker-event` CLI option or `MAKER_EVENT`. Defaults to `isp_performance_measured`.

Resin.io support
================

This project includes `Dockerfile.template` file which allows to `git push` the contents of this repository to `resin.io` repo to deploy code to a device managed by `resin.io`.

Development
===========

Run all of the unit tests and style checks:

    python setup.py test

Run the program in an isolated development Python 3.5 environment:

    python setup.py test -a "-epy35 'periodical-speedtest'"
