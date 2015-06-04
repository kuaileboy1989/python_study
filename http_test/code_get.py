#!/usr/bin/env python
#coding=utf8
 
import httplib
import urllib


def main():
    httpClient = None
    try:
        url_dic = {
                'client_id':'1430279216667',
                'response_type':'code',
                'state':'i am state',
                'redirect_uri':'http://ligj.ersoft.cn:48169/oauth/bong/redirect'
                }
        url_en = urllib.urlencode(url_dic)
        url = 'https://oauth.tbsandbox.com/authorize?'+url_en
        url = 'http://open-test.bong.cn/oauth/authorize?'+url_en
        print
        print url
        print
        httpClient = httplib.HTTPConnection(url)
        return
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
