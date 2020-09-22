# -*- coding:utf-8 -*-

SERVER_IP = ['127.0.0.1:9092', ]
TOPIC = 'test'
AUTO_OFFSET_RESET = 'latest'  # latest:最新数据开始， earliest：重头开始
CONSUMER_GROUP = 'test_group3'
API_VERSION = (2, 3, 0)


# SSL配置
SSL_SERVER_IP = ['127.0.0.1:9192', ]
SSL_CERTIFICATE = "E:\code\python\project\python-utils-class\py_kafk\com\certificate.pem"
SSL_CAFILE = "E:\code\python\project\python-utils-class\py_kafk\com\CARoot.pem"