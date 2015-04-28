#/usr/bin/env python
#-*- coding:utf8 -*-

class a(object):
    def __init__(self):
        print 'in first a'
    def __call__(self, s):
        self.test(s)
    def abc(self):
        print 'abc'
        self.test('abctest')
    def test(self, s):
        print 'in first test:',s

