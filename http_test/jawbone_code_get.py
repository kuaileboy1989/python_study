#!/usr/bin/env python
#coding=utf8
 
import httplib
import urllib


def main():
    httpClient = None
    try:
        url_dic = {
                'client_id':'jE3i9GviQfM',
                'response_type':'code',
                'state':'iamstate',
                'redirect_uri':'http://ligj.ersoft.cn/eroad_bracelet/oauth/redirect',
                'scope': 'sleep_read basic_read extended_read move_read weight_read heartrate_read'
                }
        url_en = urllib.urlencode(url_dic)
        url = 'https://jawbone.com/auth/oauth2/auth?'+url_en
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
