# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals


from mysql.base import Db
from redis.base import RedisPool


db = Db()
s = db.get_connect()
print s

redis = RedisPool()
ss = redis.get_redis()
print ss