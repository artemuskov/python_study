#!/usr/bin/env python

import urllib
import urllib2


def main():

    req = urllib2.Request('http://www.google.com/')
    with urllib2.urlopen(req) as resp:
        print 123




    # with request.urlopen('http://www.google.com/') as f:
    #     print(f.getcode())  # http response code
    #     # print(f.info())  # all header info
    #     #
    #     # resp_body = f.read().decode('utf-8')  # response body


if __name__ == "__main__":
    main()