# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import sqlalchemy
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql import text

import settings


class Db(object):

    def __init__(self, connection='default'):
        conn = settings.MYSQL_DATABASES[connection]
        mysql_uri = '{ENGINE}+mysqldb://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}?charset=utf8'.format(
            ENGINE=conn['ENGINE'],
            USER=conn['USER'],
            PASSWORD=conn['PASSWORD'],
            HOST=conn['HOST'],
            PORT=conn['PORT'],
            NAME=conn['NAME'])

        self.db = sqlalchemy.create_engine(
            mysql_uri, pool_size=36, echo=False, pool_recycle=3600)
        self.metadata = sqlalchemy.MetaData(self.db)

    def get_metadata(self):
        return self.metadata

    def get_connect(self):
        return self.db.connect()

    def get_table(self, table_name):
        return Table(table_name, self.metadata, autoload=True)

