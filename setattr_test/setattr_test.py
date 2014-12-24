#!/usr/bin/env python
#-*- coding: utf-8 -*-

class SetAttrTestClass(object):
    def __init__(self, *tp, **kw):
        self.a = 'aaa'
        setattr(self, 'b', 'bbb')
        print tp
        print kw

if __name__ == "__main__":
    test = SetAttrTestClass(1,2,3,abc=1)
    print test.a
    print test.b
