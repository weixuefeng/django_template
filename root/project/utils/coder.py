# -*- coding:utf-8 -*-
__author__ = 'weixuefeng@lubangame.com'
__version__ = ''
__doc__ = ''


import chardet


def uni_str(a, encoding=None):
    if not encoding:
        encoding = "utf-8"
    if isinstance(a, (list, tuple)):
        s = []
        for i, k in enumerate(a):
            s.append(uni_str(k, encoding))
        return s
    elif isinstance(a, dict):
        s = {}
        for i, k in enumerate(a.items()):
            key, value = k
            s[uni_str(key, encoding)] = uni_str(value, encoding)
        return s
    elif isinstance(a, str):
        return a
    elif isinstance(a, (int, float)):
        return a
    elif isinstance(a, str) or (hasattr(a, '__str__') and callable(getattr(a, '__str__'))):
        if getattr(a, '__str__'):
            a = str(a)
        return str(a, encoding)
    else:
        return a


def detect_code(content):
    try:
        encoding = chardet.detect(content)['encoding']
        encoding = encoding.upper()
        if encoding == 'GB2312':
            encoding = 'GBK'
        return encoding
    except Exception:
        return 'UTF-8'

