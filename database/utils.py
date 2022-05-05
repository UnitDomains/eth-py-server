import datetime
import uuid
from datetime import time


def get_uuid():
    """
    得到去掉‘-’的uuid
    :return:
    """
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    return suid


def adjust_hex_2_fix_length(hex_string: str):
    """
    保证16进制字符串长度为64个字符，因为有时候转换后长度不够64
    :param hex_string:0x123....，以0x打头的16进制数字
    :return:
    """

    return '0x' + hex_string[2:].zfill(64)


def date_compare_now(date1):
    """
    返回当前时间和给定时间间隔天数
    :param date1:
    :return:
    """
    time_now = datetime.datetime.now()  # 获取当前日期时间
    diff = time_now - date1
    return diff.days


def date_compare(date1, date2):
    """
    比较日期
    :param date1:第一个日期
    :param date2: 第二个日期
    :return: 如果第一个日期大于第二个日期，返回1；如果两个日期相等，返回0；如果第一个日期小于第二个日期，返回-1；意外返回其它
    """
    try:
        time1 = time.mktime(time.strptime(date1, '%Y-%m-%d'))
        time2 = time.mktime(time.strptime(date2, '%Y-%m-%d'))
        # 日期转化为int比较
        diff = int(time1) - int(time2)
        print(diff)
        if diff > 0:
            return 1
        elif diff == 0:
            return 0
        else:
            return -1
    except Exception as e:
        print(e)
        return -100
