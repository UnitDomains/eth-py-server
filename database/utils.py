import datetime
import uuid
from datetime import time


def get_uuid():
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    return suid


def adjust_hex_2_fix_length(hex_string: str):
    """
    Make sure the hexadecimal string length is 64 characters, because sometimes the conversion length is less than 64 characters
    :param hex_string:0x123....
    :return:
    """

    return '0x' + hex_string[2:].zfill(64)


def date_compare_now(date1):
    """
    Returns the current time and the number of days in the given interval
    :param date1:
    :return:
    """
    time_now = datetime.datetime.now()
    diff = time_now - date1
    return diff.days
