#!/usr/bin/env python2

# usage: python HistoricalDataRequest.py <host-ip>

import argparse
import json
import ssl
import sys
import urllib2

data = {
        "securities": ["XBT Curncy"],
        "fields": ["PX_LAST"],
        "startDate": "20120101",
        "endDate": "20150101",
        "periodicitySelection": "DAILY"
}


def request():
    req = urllib2.Request('https://http-api.openbloomberg.com/request?ns=blp&service=refdata&type=HistoricalDataRequest')
    req.add_header('Content-Type', 'application/json')

    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.load_verify_locations('bloomberg.crt')
    ctx.load_cert_chain('client.crt', 'client.key')

    try:
        res = urllib2.urlopen(req, data=json.dumps(data), context=ctx)
        print res.read()
    except Exception as e:
        e
        print e
        return 1
    return 0


def main():
    return request()

if __name__ == "__main__":
    sys.exit(main())