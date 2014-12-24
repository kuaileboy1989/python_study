#!/usr/bin/env python
#coding=utf8

from datetime import datetime

def get_time_format_now():

    now = datetime.now()

    return datetime.strftime(now, '%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    print get_time_format_now()
