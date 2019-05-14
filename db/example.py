# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

from base_mysql.base import Db
from base_redis.base import RedisPool

import os
import sys
dir_mytest = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dir_mytest)
from App_Base_Common.AppBase import AppBase, try_except
from sqlalchemy.sql import text


# db = Db()
# s = db.get_connect()
# print s
#
# redis = RedisPool()
# ss = redis.get_redis()
# print ss


class ExampleDbBase(AppBase):

    app_name = 'sor_example'

    def __init__(self):
        self.mysql_conn = Db().get_connect()
        super(ExampleDbBase, self).__init__()

    def add_arguments(self, parser):
        parser.add_argument(
            "-example",
            "--example",
            dest="example",
            help="example",
            type=int
        )

    @try_except("sor_example")
    def handle(self, options):
        sql = '''
        select * from accounts_user 
        '''
        s = self.mysql_conn.execute(text(sql=1))
        for ss in s:
            print ss


if __name__ == '__main__':
    op = ExampleDbBase()
    op.run(sys.argv)
