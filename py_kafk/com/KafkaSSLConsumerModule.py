# -*- coding:utf-8 -*-
# author：Anson
# @Time    : 2020/9/22 15:27
# @File    : KafkaSSLConsumerModule.py
from __future__ import unicode_literals

from kafka import KafkaConsumer
from conf import (SSL_SERVER_IP, TOPIC, SSL_CERTIFICATE, SSL_CAFILE,
                  API_VERSION, AUTO_OFFSET_RESET, CONSUMER_GROUP)


class KafkaSSLConsumerModule(object):

    def __init__(self, topic, bootstrap_servers, group_id, auto_offset_reset,
                 ssl_cafile, ssl_certfile):
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.auto_offset_reset = auto_offset_reset
        self.ssl_cafile = ssl_cafile
        self.ssl_certfile = ssl_certfile
        self.consumer = KafkaConsumer(self.topic,
                         bootstrap_servers=self.bootstrap_servers,
                         group_id=self.group_id,
                         security_protocol="SSL",
                         auto_offset_reset=self.auto_offset_reset,
                         ssl_check_hostname=False,
                         ssl_cafile=self.ssl_cafile,
                         ssl_certfile=self.ssl_certfile,
                         )

    def print_message(self):
        for message in self.consumer:
            print(message.value)


def main():
    print('-' * 20)
    print('消费者通过ssl加密访问')
    print('-' * 20)
    consumer = KafkaSSLConsumerModule(TOPIC, SSL_SERVER_IP, CONSUMER_GROUP,
                         AUTO_OFFSET_RESET, SSL_CAFILE, SSL_CERTIFICATE
                         )
    consumer.print_message()


if __name__ == '__main__':
    main()
