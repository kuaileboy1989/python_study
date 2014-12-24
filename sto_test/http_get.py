#!/usr/bin/env python
#coding=utf8
 
import httplib

from common_struct import *
import copy
import urllib
import urllib2
import contextlib

import simplejson
httpClient = None

params = copy.deepcopy(PARAMS)
#params = urllib.urlencode(params)
#params = simplejson.dumps(params)

'''
params = urllib.urlencode(params)
print '-----------',params
url =  'http://vip.sto.cn/STOinterfaceAction.action?'+params
print '---url:',url
req = urllib2.Request(url)
print '---req:',req
with contextlib.closing(urllib2.urlopen(req)) as res:
    print res.read()
'''

try:
    params = urllib.urlencode(params)
    httpClient = httplib.HTTPConnection('vip.sto.cn',  timeout=30)
    httpClient.request('GET', '/STOinterfaceAction.action?'+params)
#    print httpClient
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    #print response
    print response.status
    print response.reason
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
