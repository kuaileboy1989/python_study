import time
import datetime

def get_diff_hours(start, end):
    ret = 0
    
    start_list = time.strptime(start, '%Y-%m-%d %H:%M:%S')
    end_list = time.strptime(end, '%Y-%m-%d %H:%M:%S')
    start_num = time.mktime(start_list)
    end_num = time.mktime(end_list)
    diff_num = end_num - start_num
    ret = diff_num/3600.0      
    
    return ret

print get_diff_hours('2015-05-09 06:01:00', '2015-05-09 07:59:00')