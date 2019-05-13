# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals


MYSQL_DATABASES = {
    'default': {
        'ENGINE': 'mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '3306',
        'STORAGE_ENGINE': 'INNODB',
    }
}

REDIS_CONNECTION = {
    'default': {
        'HOST': '',
        'PORT': '',
        'PASSWD': '',
        'DB': 0,
    }
}

try:
    from local_settings import *
except ImportError:
    pass
