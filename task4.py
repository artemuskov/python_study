#!/usr/bin/env python

import urllib2


def main():
    req = urllib2.Request('http://ip.jsontest.com/')
    res = urllib2.urlopen(req)
    print res.info()
    res.close();


if __name__ == "__main__":
    main()