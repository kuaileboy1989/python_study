#!/usr/bin/env python
#coding=utf8
 
import httplib
import urllib


def main():
    httpClient = None
    try:
        url_dic = {
                'client_id':'2882303761517363095',
                'response_type':'code',
                'state':'iamstate',
                'redirect_uri':'http://ligj.ersoft.cn/eroad_bracelet/oauth/redirect',
                }
        url_en = urllib.urlencode(url_dic)
        url = 'https://account.xiaomi.com/oauth2/authorize?'+url_en
        print
        print url
        print
        return


        httpClient = httplib.HTTPConnection(url)
        httpClient.request('GET', '/')
    
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

if __name__ == "__main__":
    main()
