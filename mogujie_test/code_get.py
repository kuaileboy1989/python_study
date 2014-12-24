#!/usr/bin/env python
#coding=utf8
 
import httplib
import urllib


def main():
    httpClient = None
    try:
        url_dic = {
                'app_key':'e35ab43d1de7312212398b7d84458c7d',
                'response_type':'code',
                'redirect_uri':'http://biz.ex-sandbox.com/callback.php'
                }
        url_en = urllib.urlencode(url_dic)
        url = 'https://www.mogujie.com/openapi/api_v1_oauth/index?'+url_en
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
