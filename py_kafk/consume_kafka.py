# -*- coding: utf-8 -*-
'''
@author: anson
@file: consume_kafka.py
@time: 2020/03/24 15:20
'''
from __future__ import unicode_literals

import pykafka
import time


class KafkaReaderThread(object):
    def __init__(self, hosts, broker_version, topic, consumer_group):
        self.hosts = hosts
        self.broker_version = broker_version
        self.topic = topic
        self.consumer_group = consumer_group
        self.client = self.new_client()

    def new_client(self):
        print "start connect..."
        try:
            new_client = pykafka.KafkaClient(
                hosts=self.hosts,
                # zookeeper_hosts=self.proc_setting['setting']['zk_server'],
                broker_version=self.broker_version
            )
            print "connected"
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
                    # auto_commit_enable=True,
                    # auto_commit_interval_ms=1
                    # reset_offset_on_start=False,
                    # auto_offset_reset=pykafka.common.OffsetType.LATEST,
                )
                # print topic.partitions
                consumer.start()
                # _offset = consumer.held_offsets()
                for message in consumer:
                    # test modle

                    print("message_value:", message.value)
                    print("consumer_held_offsets:", consumer.held_offsets)

                    consumer.commit_offsets()
                    # consumer.stop()
                    # continue

            except Exception as e:
                print("error: {}".format(e))
                try:
                    consumer.stop()
                except Exception as e:
                    pass


if __name__ == '__main__':
    # 获取毫秒时间戳
    t = time.time()
    hosts = "192.168.199.132:9092"
    broker_version = '2.3.0'
    topic = "test1"
    consumer_group = "consumer_group_police_seemmo"
    kafka = KafkaReaderThread(hosts, broker_version, topic, consumer_group)
    while 1:
        if kafka.client:
            kafka.fetchmany()