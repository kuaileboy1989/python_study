#!/usr/bin/env python
#coding=utf8
 
import httplib, urllib

import hashlib
import time
import datetime
import copy

from common_struct import *
#from utils import *
from common_xml import xml

#######################################
def params_trans_xml():
    result_dic = get_api_params()
    #result_dic.update(result_dic_sys)
    sign_dic = get_api_sign(result_dic)
    params = dict(result_dic,**sign_dic)
    params.update(xml)
    return params


def get_api_params():
    result_dic = {}
#result_dic['gShopID'] = msg.get('dangdang_shop_id','')
    result_dic['method'] = 'dangdang.order.goods.send'
    result_dic['app_key'] = '2100000613'
    result_dic['format'] = 'xml'
    result_dic['v'] = '1.0'
    result_dic['sign_method'] = 'md5'
    result_dic['session'] = '78011FE0EF6BCC4CEEDF35C5D28A2930AC715B2CDF172569672C5CCDA5423407'
    result_dic['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return result_dic

def get_api_sign(sign_msg):
    res = {}
#    token = req.get('dangdang_api_secrt')
    token = 'B2CED651D2D58BF4230C23026A298932'
    res['sign'] = get_dangdang_sign_str(token,sign_msg)
    return res

def get_dangdang_sign_str(seckey,params):
    l = sorted(params.iteritems(), key=lambda x:x[0])
    sign_str = ''
    for k,v in l:
        sign_str = sign_str+k+v
    s = '%s%s%s' % (seckey, sign_str, seckey)
    print get_md5(s).upper()
    return get_md5(s).upper()

def get_md5(string):
    try:
        m = hashlib.md5()
        m.update(string)
        dest = m.hexdigest()
        return dest
    except:
        return False


#######################################


def main():
    httpClient = None
    token = TOKEN
    try:
#params = copy.deepcopy(STORE_ITEM_SPECS_GET)
#        params['timestamp'] = get_time_format_now()
#        params['sign'] = gen_matrix_sign(params,token)
        #        params = urllib.urlencode({'from_node_id': '1','to_node_id': '2','sign':'aaaaaaaa','method':'abc'})
        params = params_trans_xml()
        print '\n---:',params
        params = urllib.urlencode(params)
        print '\n---:',params
#    return
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
                                     
#        httpClient = httplib.HTTPConnection("localhost", 18672, timeout=30)
        #rpc_sf_wms
#        httpClient = httplib.HTTPConnection("localhost", 18687, timeout=30)
        httpClient = httplib.HTTPConnection("api.open.dangdang.com", timeout=30)
#        httpClient = httplib.HTTPConnection("192.168.75.118", 1888, timeout=30)
#        httpClient = httplib.HTTPConnection("matrix.ecos.shopex.cn", timeout=30)
        httpClient.request("POST", "/openapi/rest", params, headers)
#        params = urllib.urlencode(xml)
#        httpClient.request("POST", "/sf_wms_notify?erp_node=1833323732&sf_wms_node=1738363832", params, headers)
                                             
        response = httpClient.getresponse()
        print '\n---:',response.status
        print '\n---:',response.reason
        res = response.read()
        print '\n---:',res
        print '\n---:',res.decode('gbk').encode('utf8')
        print '\n---:',response.getheaders() #获取头信息
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
