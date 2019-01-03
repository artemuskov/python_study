#!/usr/bin/env python

import urllib2


def main():
    response = urllib2.urlopen('http://ip.jsontest.com/')
    print response.info()
    response.close()


if __name__ == "__main__":
    main()