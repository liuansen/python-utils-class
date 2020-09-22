# -*- coding:utf-8 -*-
# author：Anson
# @Time    : 2020/9/21 14:36
# @File    : encrypt_kafka.py
from __future__ import unicode_literals

from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json


class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        """
        只要检查到了是bytes类型的数据就把它转为str类型
        :param obj:
        :return:
        """
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

class Kafka_producer():
    '''
    使用kafka的生产模块
    '''
    def __init__(self, kafkahost,kafkaport, kafkatopic):
        ssl_certfile = "../conf/certificate.pem"
        ssl_cafile = "../conf/ca-root.pem"
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        self.producer = KafkaProducer(
            bootstrap_servers="localhost:9092",
            value_serializer=lambda v: json.dumps(v, cls=MyEncoder,indent=4).encode('utf-8'),
            retries=0,
            api_version = (2, 3),
            request_timeout_ms=200,
            ssl_check_hostname=False,
            ssl_certfile=ssl_certfile,
            security_protocol="SSL",
            ssl_cafile=ssl_cafile
        )

    def sendjsondata(self, params):
        try:
            parmas_message = json.dumps(params)
            print(parmas_message)
            producer = self.producer
            producer.send(self.kafkatopic, parmas_message.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            print(e)


class Kafka_consumer():
    '''
    使用Kafka—python的消费模块
    '''

    def __init__(self, kafkahost, kafkaport, kafkatopic, groupid):
        ssl_certfile = "../conf/certificate.pem"
        ssl_cafile = "../conf/ca-root.pem"
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        self.groupid = groupid
        self.consumer = KafkaConsumer(group_id="consumer_group_police_seemmo",
                                      bootstrap_servers = '127.0.0.1:9092',
                                      api_version=(2, 3),
                                      enable_auto_commit=False,
                                      auto_commit_interval_ms=5000,
                                      # ssl_check_hostname=False,
                                      # ssl_certfile=ssl_certfile,
                                      # security_protocol="SSL",
                                      # ssl_cafile=ssl_cafile
        )
    def consume_data(self):
        print('123')
        self.consumer.subscribe(['test'])
        try:
            for message in self.consumer:
                print(json.loads(message.value))
        except KeyboardInterrupt as e:
            print(e)


if __name__ == '__main__':
    '''
    测试consumer和producer
    :return:
    '''
    # # 测试生产模块
    # producer = Kafka_producer("127.0.0.1", 9092, "test")
    # for i in range(10):
    #    params = '{abetst}:{null}---'+str(i)
    #    producer.sendjsondata(params)

    # 测试消费模块
    # consumer = Kafka_consumer("127.0.0.1", 9092, "test", "asklfdjsdfasdfg")
    # consumer.consume_data()
    # print type(self.bootstrap_servers)

    consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092'],group_id='wm_group', auto_offset_reset='latest', enable_auto_commit=False)
    consumer.subscribe(['test'])  #订阅要消费的主题

    # print consumer.topics()
    # print "+++++++",consumer.position(TopicPartition(topic=u'ctripapi_duplicateddata_review', partition=1)) #获取当前主题的最新偏移量

    for message in consumer:
        print(message.value)