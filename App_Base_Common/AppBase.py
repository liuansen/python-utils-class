# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import sys
from argparse import ArgumentParser
from functools import wraps
from raven import Client
from settings import SENTRY_URL
from log import get_logger


class AppBase(object):
    help = ''
    app_name = 'app_base'

    def create_parse(self, sub_command):
        parser = ArgumentParser(
            prog='%s' % sub_command, description=self.help or None
        )
        self.add_arguments(parser)
        return parser

    def add_arguments(self, parser):
        """
        增加参数
        :param parser:
        :return:
        """
        pass

    def app_init(self):
        """
        应用初始化
        :return:
        """
        pass

    def get_db_data(self):
        """
        得到数据库表信息
        :return:
        """
        return

    def run(self, args):
        parser = self.create_parse(args[0])
        options = parser.parse_args(args[1:])
        cmd_options = vars(options)

        self.app_init()
        self.handle(cmd_options)

    def handle(self, options):
        """
        处理函数
        :param options:
        :return:
        """
        pass


def get_sentry_client():
    client = Client(SENTRY_URL)
    return client


def try_except(log_name=None):
    def decorator_try(func):
        @wraps(func)
        def exception_handle(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                log = get_logger(log_name)
                log.error(e, exc_info=True)
                client = get_sentry_client()
                client.captureException()
            finally:
                pass

        return exception_handle

    return decorator_try
