# -*- coding:utf-8 -*-
# author：Anson
# @Time    : 2020/9/22 15:27
# @File    : KafkaSSProducerModule.py
from __future__ import unicode_literals

from kafka import KafkaProducer
from conf.settings import SSL_SERVER_IP, TOPIC, SSL_CERTIFICATE, SSL_CAFILE, API_VERSION


class KafkaSSProducerModule(object):
    def __init__(self, topic, ssl_server_ip, api_version, ssl_certificate, ssl_cafile):
        self.topic = topic
        self.ssl_server_ip = ssl_server_ip
        self.api_version = api_version
        self.ssl_certificate = ssl_certificate
        self.ssl_cafile = ssl_cafile
        self.producer = KafkaProducer(
                        bootstrap_servers=self.ssl_server_ip,
                        retries=0,
                        api_version = self.api_version,
                        request_timeout_ms=1000,
                        ssl_check_hostname=False,
                        ssl_certfile=self.ssl_certificate,
                        security_protocol="SSL",
                        ssl_cafile=self.ssl_cafile
                    )

    def producer_send(self, params):
        producer = self.producer
        producer.send(self.topic, params)
        producer.flush()


def main():
    print('-' * 20)
    print('生产者通过ssl加密访问')
    print('-' * 20)
    future = KafkaSSProducerModule(TOPIC, SSL_SERVER_IP, API_VERSION, SSL_CERTIFICATE, SSL_CAFILE)
    for id in range(10):
        params = bytes(("Hello World SSL-{0}".format(str(id))).encode('utf-8'))
        print(params)
        future.producer_send(params)


if __name__ == '__main__':
    main()
