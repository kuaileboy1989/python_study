# -*- coding: utf-8 -*-

import cPickle as pickle
import struct
import sys

cs1 = {
    'a_str10': 'aa',
    'b_int': 100
}
cs2 = {
    'a_str10': 'aaaaddddddddddddddddddddddddddddddddd',
    'b_int': 10
}

bytes1 = struct.pack('i', cs1['b_int'])
len_b1 = len(bytes1)
print '====len_b1:', len_b1, sys.getsizeof(cs1)
bytes2 = struct.pack('10si', cs2['a_str10'], cs2['b_int'])
len_b2 = len(bytes2)
print '====len_b2:', len_b2, sys.getsizeof(cs2)

#f = open('bytes.txt', 'ab')
#f.write(bytes1)
#f.write(bytes2)
#f.close()
#
#f1 = open('bytes.txt', 'rb')
#
##读取第几个
#i = 2
#
#f1.seek(16*(i-1))
#rb = f1.read(16)
#f.close()
#
#a, b = struct.unpack('10si', rb)
#print a, b

#class a:
#    def __init__(self, a, b):
#        self.a = a
#        self.b = b
#    def p(self):
#        print 'i am in a !!!'
#        
#class a1:
#    def __init__(self):
#        pass
#    def p(self):
#        print 'i am in a1 !!!'

#b = a()
#
#bytes = struct.pack('%ss'%(len(str(b))), str(b))
#
#print '==bytes:', bytes, len(bytes)
#f = open('bytes.txt', 'wb')
#f.write(bytes)
#f.close()
#
#f1 = open('bytes.txt', 'rb')
#res = f1.read()
#f1.close()
#
#print '===f1 pack:', res, len(res)
#print '===f1 unpack:', struct.unpack('%ss'%len(res), bytes)

#b = a('aa', 'bb')
#b1 = a('aaa', 'bbb')
#
#f = open('dump.txt', 'wb')
#bd = pickle.dumps(b)
#print '===len(bd):',len(bd)
#len_bd = len(bd)
#
#f.write(bd)
#bd1 = pickle.dumps(b1)
#print '===len(bd1):',len(bd1)
#len_bd1 = len(bd1)
#f.write(bd1)
#f.close()
#
#f1 = open('dump.txt', 'rb')
#d1 = f1.read(len_bd)
#obj1 = pickle.loads(d1)
#d2 = f1.read(len_bd1)
#obj2 = pickle.loads(d2)
#f1.close()
#
#obj1.p()
#print obj1.a
#obj2.p()
#print obj2.a
