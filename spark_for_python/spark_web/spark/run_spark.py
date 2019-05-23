# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession


class SparkWeb(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(SparkWeb, cls).__new__(cls)

        return cls.instance

    def __init__(self, app_name='spark_web'):
        if SparkWeb.init_flag:
            return
        else:
            spark_conf = SparkConf().setAppName(app_name)
            self.spark_context = SparkContext(conf=spark_conf)
            self.spark_session = SparkSession(self.spark_context)
        print('初始化spark{app_name}'.format(app_name=app_name))
        SparkWeb.init_flag = True
    pass

