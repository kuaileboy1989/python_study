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
                #'date': time.time(),
                #'page_token': 1,
                #'start_time': time.time(),
                #'end_time': time.time(),
                #'updated_after': time.time(),
                }

def main():
    httpClient = None
    #token = TOKEN
    try:
        #params = copy.deepcopy(TOKEN_GET_STRUCT)
        #        params = urllib.urlencode({'from_node_id': '1','to_node_id': '2','sign':'aaaaaaaa','method':'abc'})
        #print '\n---:',params
        #params = urllib.urlencode(params)
        #params = simplejson.dumps(params)
        #print '\n---:',params
        url = 'https://jawbone.com/nudge/api/v.1.1/users/@me'
        print '\n----url:', url
        headers = {"Accept": "application/json",
                   "Authorization": "Bearer DudD7GQwFnf2uxTX_5b5vb4dpkSA0mjuPZJXREh5iPkA_6kc79HQJCOqZFfWkiyWcqtj6bMtuuJMWLqfgbkSwFECdgRlo_GULMgGZS0EumxrKbZFiOmnmAPChBPDZ5JP"}
#        print response.read()
        req = urllib2.Request(url, headers=headers)
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
