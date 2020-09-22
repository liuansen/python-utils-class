# -*- coding: utf-8 -*-
'''
@author: anson
@file: consume_kafka.py
@time: 2020/03/24 15:20

*/1 * * * * flock -xn /home/anson/python/code/python_kafka/consume_kafka.lock -c 'python /home/anson/python/code/python_kafka/consume_kafka.py'
'''
from __future__ import unicode_literals

import pykafka
import datetime
import time
from pykafka import SslConfig


FILE_PATH = '/home/anson/python/code/python-utils-class/py_kafk/tencent_waf' 
hosts = "127.0.0.1:9092"
broker_version = '2.3.0'
topic = "test"
consumer_group = "consumer_group_police_seemmo"


class KafkaReaderThread(object):
    def __init__(self, hosts, broker_version, topic, consumer_group):
        self.hosts = hosts
        self.broker_version = broker_version
        self.topic = topic
        self.consumer_group = consumer_group
        self.client = self.new_client()

    def new_client(self):
        print("start connect...")
        try:
            new_client = pykafka.KafkaClient(
                hosts=self.hosts,
                broker_version=self.broker_version
            )
            print("connected")
            return new_client
        except Exception as e:
            print("error: {}".format(e))
            return

    def fetchmany(self):
        client = self.client
        if client:
            consumer = None
            try:
                topic = client.topics[self.topic]

                consumer = topic.get_balanced_consumer(
                    consumer_group=self.consumer_group,
                    managed=True,
                    auto_start=False,
                    auto_commit_enable=True,
                    auto_commit_interval_ms=1,
                    reset_offset_on_start=False,
                    auto_offset_reset=pykafka.common.OffsetType.LATEST,
                )
                consumer.start()
                for message in consumer:
                    print(message.value)
                #     # file_tsName = str(int(time.mktime(time.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H'), '%Y-%m-%d %H')))*1000)
                #     # file_paths = FILE_PATH + '/' + 'tencent_waf_' + file_tsName + '.dat'
                #     # with open(file_paths,'a') as f:
                #     #     f.write(message.value + '\n')

                    consumer.commit_offsets()

            except Exception as e:
                print("error: {}".format(e))
                try:
                    consumer.stop()
                except Exception as e:
                    pass
    
    def writedata(self, pro_message):
        client = self.client
        if client:
            try:
                topic = client.topics[self.topic]
            except Exception as e:
                print("error: {}".format(e))
            with topic.get_sync_producer() as producer:
                producer.produce(bytes(pro_message, encoding='utf-8'))

if __name__ == '__main__':
    kafka = KafkaReaderThread(hosts, broker_version, topic, consumer_group)
    pro_messages = ['zhang', 'liu', 'zheng', 'li', 'wang', 'zhou', 'jiang', 'wu', 'shangguan', 'aixinjueluo']
    if kafka.client:
        # kafka.fetchmany()
        for pro in pro_messages:
            kafka.writedata(pro)
