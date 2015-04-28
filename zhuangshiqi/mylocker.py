#-*- coding:utf8 -*-
'''
   公共类 for 示例9
'''

class mylocker:
    def __init__(self):
        print ("mylocker.__init__() called.")

    @staticmethod
    def acquire():
        print ("mylocker.acquire() called.")

    @staticmethod
    def unlock():
        print ("mylocker.unlock() called.")

class lockerex(mylocker):

    @staticmethod
    def acquire():
        print ("lockerex.acquire() called.")

    @staticmethod
    def unlock():
        print ("lockerex.unlock() called")

def lockhelper(cls):
    '''
        cls 必须实现acquire和unlock静态方法
    '''
    def _deco(func):
        def __deco(*args, **kwargs):
            print('before %s called [%s].'%(func.__name__, cls))
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()
        return __deco
    return _deco
