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
                'yyyymmdd':'20150628',
                'uid':'33623950369539523785',
                'access_token':'b9a82f9a-d6a6-4339-867d-e1b4e243275e'
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
        #url = 'http://open-test.bong.cn/1/sleep/blocks/20150504/3?uid=85977285743145918548&access_token=a820493f-7932-4c6a-930a-8e2af536307c'
        url = 'http://open.bong.cn/1/sleep/blocks/20150628/3?uid=33623950369539523785&access_token=b9a82f9a-d6a6-4339-867d-e1b4e243275e'
#        print response.read()
        resp = urllib2.urlopen(url)
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
