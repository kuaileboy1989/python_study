#!/usr/bin/env python
# -*- coding:UTF-8 -*-

ori_list = [[], ['a', 'b', 'c'], [],  [1, 2, 3], [11, 22, 33, 44], [111, 222]]

ori_list = [['a', 'b', 'c'], [1, 2, 3], [11, 22, 33, 44], [111, 222], ['aa', 'bb']]

#now: [[], [], []...]
#next: [X, X, X...]
def foo(now, next):
    ret = []
    for i in next:
        for j in now:
            ret.append(j + [i])

    return ret

def main():
    new_list = []
    #因为空列表在计算中没有实际意义，可以首先去空
    for i in ori_list:
        if i:
            new_list.append(i)
    print new_list
    LEN = len(new_list)
    now = []

    for i in new_list[0]:
        now.append([i])

    for i in range(LEN):
        if i+1 == LEN:
            res = now
        else:
            res = foo(now, new_list[i+1])
            now = res
    for i,item in enumerate(res):
        print item,
        if (i+1)%3 == 0:
            print '\n'

    print 'total num:',len(res)

if __name__  == '__main__':
    main()
