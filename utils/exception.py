# coding:       utf-8
# @Author:      u14e
# @Time:        2019/07/26 01:05
# @Description: 自定义异常
from rest_framework.exceptions import APIException
from rest_framework import status


class BadRequestError(APIException):
    """
    错误请求
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '无效输入'
    default_code = 'invalid'
