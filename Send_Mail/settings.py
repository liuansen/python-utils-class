# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

MAIL_SMTP = ''
MAIL_HOST = ''
MAIL_USER = ''
MAIL_PWD = ''

try:
    from local_settings import *
except ImportError:
    pass
