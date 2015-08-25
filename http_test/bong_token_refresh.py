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
                'client_id':'1430279216667',
                'client_secret':'5a9c2fa999d74ec99cd8ed91d72e7a2d',
                'grant_type':'refresh_token',
                'refresh_token':'188d1397-ba85-4d6a-98ec-007cf791f650'
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
        url = 'https://open.bong.cn/oauth/token'
#        print response.read()
        resp = urllib2.urlopen(url, params)
        print '\n---response:'
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
