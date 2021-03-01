# -*- coding:utf-8 -*-

SERVER_IP = ['127.0.0.1:9092', ]      # kafka集群地址，用逗号分隔
TOPIC = 'test2'                       # kafka要消费的topic
AUTO_OFFSET_RESET = 'latest'          # latest:最新数据开始， earliest：重头开始
CONSUMER_GROUP = 'test_group33'       # 消费组
API_VERSION = (2, 3, 0)               # kafka版本


# SSL配置
SSL_SERVER_IP = ['127.0.0.1:9192', ]
# kafka生产的签名文件
SSL_CERTIFICATE = "E:\code\python\project\python-utils-class\py_kafk\conf\certificate.pem"
SSL_CAFILE = "E:\code\python\project\python-utils-class\py_kafk\conf\CARoot.pem"