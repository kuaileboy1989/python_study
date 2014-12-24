#!/usr/bin/env python
#coding=utf8
 
import httplib, urllib

import hashlib
import time
import copy
import traceback
from common_struct import *
from utils import *
from common_xml import xml

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
        params = copy.deepcopy(STORE_ITEM_SPECS_GET)
        params['timestamp'] = get_time_format_now()
        params['sign'] = gen_matrix_sign(params,token)
        #        params = urllib.urlencode({'from_node_id': '1','to_node_id': '2','sign':'aaaaaaaa','method':'abc'})
        print '\n---:',params
        params = urllib.urlencode(params)
        print '\n---:',params
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
                                     
        httpClient = httplib.HTTPConnection("localhost", 18672, timeout=30)
        #cloud_api测试
#        httpClient = httplib.HTTPConnection("192.168.75.119", 18989, timeout=30)
#        httpClient = httplib.HTTPConnection("matrix.ecos.shopex.cn", timeout=30)
        #rpc_sf_wms
#        httpClient = httplib.HTTPConnection("localhost", 18687, timeout=30)
#        httpClient = httplib.HTTPConnection("matrix_notify.ex-sandbox.com", timeout=30)
#        httpClient = httplib.HTTPConnection("192.168.75.118", 1888, timeout=30)
#        httpClient = httplib.HTTPConnection("matrix.ecos.shopex.cn", timeout=30)
#        httpClient.request("POST", "/sync", params, headers)
#        params = urllib.urlencode(xml)
#       httpClient.request("POST", "/sf_wms_notify?erp_node=1833323732&sf_wms_node=1738363832", params, headers)
        httpClient.request("POST", "/sync", params, headers)
#        httpClient.request("POST", "/cloudapi", params, headers)
                                             
        response = httpClient.getresponse()
        print '\n---:',response.status
        print '\n---:',response.reason
        res = response.read()
        print '\n---:',res
        print '\n---:',response.getheaders() #获取头信息
    except Exception, e:
        print e
        print traceback.print_exc(5)
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
