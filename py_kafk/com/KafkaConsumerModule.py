# -*- coding:utf-8 -*-
# author：Anson
# @Time    : 2020/9/21 14:40
# @File    : settings.py
from __future__ import unicode_literals

from kafka import KafkaConsumer

from conf import SERVER_IP, TOPIC, AUTO_OFFSET_RESET, CONSUMER_GROUP, API_VERSION


class KafkaConsumerModule(object):
    def __init__(self, bootstrap_servers, auto_offset_reset, topic, group_id, api_version):
        self.bootstrap_servers = bootstrap_servers
        self.auto_offset_reset = auto_offset_reset
        self.topic = topic
        self.group_id = group_id
        self.api_version = api_version
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset=self.auto_offset_reset,
            group_id=self.group_id,
            session_timeout_ms=6000,
            heartbeat_interval_ms=2000,
            api_version=self.api_version,
            enable_auto_commit=False
        )

    def print_message(self):
        messages = self.consumer
        for message in messages:
            print(message.value)


def main():
    print('-' * 20)
    print('消费者')
    print('-' * 20)
    consumer = KafkaConsumerModule(SERVER_IP, AUTO_OFFSET_RESET, TOPIC, CONSUMER_GROUP, API_VERSION)
    consumer.print_message()


if __name__ == '__main__':
    main()
    