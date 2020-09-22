# -*- coding:utf-8 -*-
# author：Anson
# @Time    : 2020/9/21 14:40
# @File    : settings.py
from __future__ import unicode_literals

import datetime
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

from conf import SERVER_IP, TOPIC


class KafkaProducerModule(object):

    def __init__(self, bootstrapServers, kafkaTopic):
        self.bootstrapServers = bootstrapServers
        self.kafkaTopic = kafkaTopic
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrapServers)

    def sendjsondata(self, params):
        try:
            parmas_message = json.dumps(params)
            producer = self.producer
            future = producer.send(self.kafkaTopic, parmas_message.encode('utf-8'))
            producer.flush()
            recordMetadata = future.get(timeout=10)
            print(params)
            print(recordMetadata, datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        except KafkaError as e:
            print(e)


def main():
    bootstrapServers = SERVER_IP
    topicStr = TOPIC

    print('-' * 20)
    print('生产者')
    print('-' * 20)

    producer = KafkaProducerModule(bootstrapServers, topicStr)
    for id in range(10):
        params = '{test data}:{no encryption data}---' + str(id)
        producer.sendjsondata(params)


if __name__ == '__main__':
    main()
    