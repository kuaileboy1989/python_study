#!/usr/bin/env python
#coding=utf8
 
import httplib, urllib2
import urllib
import hashlib
import time
import copy

from common_struct import *
from utils import *

def md5(key):
    """
        # 生成md5加密串
        #
        # @param    string key 待加密字符串
        # @return   string 已加密字符串
        # @todo
    """
    hash = hashlib.md5()
    hash.update(key)
    return hash.hexdigest()

def ksort(data,rev=False):
    """
        # 对字典/列表按照键名排序
        #
        # @param    dict/list data 字典/列表对象
        # @param    bool rev 反向排序
        # @return   list each item is a tuple that contains (key,value)
        # @todo
    """
    return sorted(enumerate(data) if isinstance(data,list) else data.items(),key=lambda x:x[0],reverse=rev)

def assemble(params):
    """
        # 组合签名参数
        #
        # @param   dict/list params
        # @return  str
        # @todo
    """
    sort_params = ksort(params)
    sign_str = ''
    for k,v in sort_params:
        sign_str += '%s%s' % (k,assemble(v) if isinstance(v,(dict,list)) else v)
    return sign_str

def gen_matrix_sign(params,token):
    """
        # 生成矩阵签名
        #
        # @param   dict/list params
        # @param   str token
        # @return  str
        # @todo
    """
    return md5((md5(assemble(params)).upper()+token)).upper()

def main():
    httpClient = None
    token = TOKEN
    try:
        params = copy.deepcopy(TOKEN_GET_STRUCT)
        #        params = urllib.urlencode({'from_node_id': '1','to_node_id': '2','sign':'aaaaaaaa','method':'abc'})
        print '\n---:',params
        params = urllib.urlencode(params)
        print '\n---:',params
        url = "https://www.mogujie.com/openapi/api_v1_accesstoken/index"
#        req = urllib2.Request("https://oauth.tbsandbox.com/token")
#        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
#        response = opener.open(req, params)
#        print response.read()
        resp = urllib2.urlopen(url, params)
        print resp.read()
        ''' headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
                                     
        httpClient = httplib.HTTPConnection("https://oauth.tbsandbox.com")
        httpClient.request("POST", "/token", params, headers)
                                             
        response = httpClient.getresponse()
        print '\n---:',response.status
        print '\n---:',response.reason
        res = response.read()
        print '\n---:',res
        print '\n---:',response.getheaders() #获取头信息'''
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
