#/usr/bin/env python
#-*- coding:utf8 -*-
import aa

def cover(self, s):
    print 'cover:',s

obj = aa.a()
aa.a.test = cover

obj.abc()

obj('call')
