#!/usr/bin/env python
#coding=utf8
 
import httplib
import urllib
import httplib, urllib2
import urllib
import hashlib
import time
import copy

from utils import *

        
TOKEN_GET_STRUCT = {
                'client_id':'jE3i9GviQfM',
                'client_secret':'aa14a52c2c8238e1269092ffc9e35870e055587e',
                'grant_type':'refresh_token',
                'refresh_token':'r3RGUZJLx_t2BN5oyP5niE94KuwAqCJ0lx_NdM_Bme7dL2WxNgQvKekaCy5aBtavNNWfJhnfRQwlAN2iCODyqw'
                }


def main():
    httpClient = None
    #token = TOKEN
    try:
        params = copy.deepcopy(TOKEN_GET_STRUCT)
        #        params = urllib.urlencode({'from_node_id': '1','to_node_id': '2','sign':'aaaaaaaa','method':'abc'})
        print '\n---:',params
        params = urllib.urlencode(params)
        print '\n---:',params
        url = 'https://jawbone.com/auth/oauth2/token'
#        print response.read()
        resp = urllib2.urlopen(url, params)
        print resp.read()
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
