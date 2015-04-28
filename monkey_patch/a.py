#/usr/bin/env python
#-*- coding:utf8 -*-

class a(object):
    def __init__(self):
        print 'in first a'
    def test(self, s):
        print 'in first test:',s
    def abc(self):
        print 'abc'

def cover(self, s):
    print 'cover:',s

a.test = cover

obj = a()
obj.test('cover')
