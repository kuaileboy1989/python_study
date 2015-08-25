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
                'appid': '2882303761517364240',
                'third_appid': '1437543634',
                'third_appsecret': 'ODY0YzRiY2Q4NmVjNGMwODBiMDAxNDAxNGJlZTVlYTQ',
                'mac_key': 'W-U33g_5kzDma6WoLckg6tBJstM',
                'call_id': time.time(),
                'access_token': 'V2_KMwuTr7D-QDD8wQ36Ks6YXV3q2OhXdkai7P1-z6Bd0pXHBq_nA8CF_SghNDfz3cLoWNp5xdAZLkJ_qouE7tIoEGgTYsHbP-MDcjN2Eq9CHjQPdRdem_IQBoim6uYmk39',
                'fromdate': '2015-08-05',
                'todate': '2015-08-10',
                'v': '1.0',
                'l': 'english'
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
        url = 'https://hmservice.mi-ae.com.cn/user/summary/getData'
#        print response.read()
        print url+'?'+params
        resp = urllib2.urlopen(url+'?'+params)
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
