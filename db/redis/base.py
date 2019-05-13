# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import settings
import redis


class RedisPool(object):

    def __init__(self, conf='default'):
        redis_config = settings.REDIS_CONNECTION[conf]
        print redis_config
        self.pool = redis.ConnectionPool(host=redis_config['HOST'],
                                         port=redis_config['PORT'],
                                         password=redis_config['PASSWD'])

    def get_pool(self):
        return self.pool

    def get_redis(self):
        return redis.Redis(connection_pool=self.pool)

    def get_pipeline(self):
        redis_config = settings.REDIS_CONNECTION['default']
        return redis.Redis(
            host=redis_config['HOST'], port=redis_config['PORT'],
            password=redis_config['PASSWD']).pipeline()
