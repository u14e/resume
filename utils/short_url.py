# coding:       utf-8
# @Author:      u14e
# @Time:        2019/07/23 21:19
# @Description: 短网址相关的工具函数
import string

# 62个字符(数字(10) + 小写字母(26) + 大写字母(26))
CHARS = string.digits + string.ascii_lowercase + string.ascii_uppercase


def encode(num):
    """十进制转换为62进制"""
    if num == 0:
        return CHARS[0]
    unit = len(CHARS)
    res = []
    while num:
        rest = num % unit
        res.insert(0, CHARS[rest])
        num = num // unit
    return ''.join(res)


def test_encode():
    """
    https://tool.lu/hexconvert/
    """
    assert encode(0) == '0'
    assert encode(63) == '11'
    assert encode(201314) == 'Qn0'
