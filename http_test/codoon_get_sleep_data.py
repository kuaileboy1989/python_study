#!/usr/bin/env python
#coding=utf8
 
import httplib
import urllib
import httplib, urllib2
import urllib
import hashlib
import time
import copy
import simplejson
import contextlib

from utils import *

        
TOKEN_GET_STRUCT = {
                'the_day':'2015-06-05',
                }


def main():
    httpClient = None
    #token = TOKEN
    try:
        params = copy.deepcopy(TOKEN_GET_STRUCT)
        #        params = urllib.urlencode({'from_node_id': '1','to_node_id': '2','sign':'aaaaaaaa','method':'abc'})
        #print '\n---:',params
        #params = urllib.urlencode(params)
        params = simplejson.dumps(params)
        print '\n---:',params
        url = 'http://api.codoon.com/api/get_sleep_data'
        headers = {"Authorization": "Bearer 7f4864f576f81a7e5455134cb05d6795"}
#        print response.read()
        req = urllib2.Request(url, params, headers)
        with contextlib.closing(urllib2.urlopen(req)) as res:
            resp = res.read()
        #resp = urllib2.urlopen(url)
        print '\n---response:'
        print resp
        print type(resp)
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

if __name__ == "__main__":
    print '-'*30
    main()
    print '-'*30
#    print '*'*30
#    print md5('1234')
#    data = {'b':'2','a':'1','c':'3'}
#    params = {'b':'2','a':'1','c':'3'}
#    token = '1234567890'
#    print ksort(data,rev=False)
#    print assemble(params)
#    print gen_matrix_sign(params,token)
#    print '*'*30
