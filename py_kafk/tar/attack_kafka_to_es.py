#!/usr/bin/env python
# -*- coding:utf-8 -*-
#read waf accesslog and attacklog from kafka to elasticsearch
import sys
import json
import copy
import time
import pykafka
import datetime
import traceback
import threading

from threading import Timer
from elasticsearch import helpers
test1tes
test1tessfsd
from elasticsearch import Elasticsearch

reload(sys)
sys.setdefaultencoding("utf-8")

lock = None
send_timer = None

class Kafka2ES(object):
    def __init__(self, host = '10.253.82.224:9092,10.253.82.95:9092,10.253.82.96:9092', topic = 'log'):
        global lock
        self.data = []
        self.host = host
        self.topic = topic
        self._index = "attack_log" if topic == "log" else "access_log"

        self.client = pykafka.KafkaClient(hosts = self.host)
        self._topic = self.client.topics[topic]
        self._consumer = self._topic.get_balanced_consumer("%s_kafka_to_es11" % (topic), managed = True, auto_offset_reset = OffsetType.LATEST)

        self.es = Elasticsearch([{"host":"127.0.0.1"}]) #default connect to localhost:9200
       
       
        lock = threading.Lock()

    def access_decode(self, msg):
        return msg

    def attack_decode(self, msg):
        t = time.mktime(datetime.datetime.strptime(msg["local_time"], "%Y-%m-%d %H:%M:%S").timetuple())
        utc_t = datetime.datetime.utcfromtimestamp(t)
        msg["@timestamp"] = utc_t.isoformat()
        status = msg["status"]
        source = int(msg.get("source", 0))
        if status == 1:
            msg["status"] = "拦截"
        else:
            msg["status"] = "观察"
        if source == 4:
            msg["rule_msg"] = "CC攻击"
        return msg

    def _decode(self, msg):
        msg = json.loads(msg.decode("latin-1"), encoding = "utf-8")
        if self.topic == "log":
            return self.attack_decode(msg)

        return self.access_decode(msg)

    def run(self):
        global send_timer
        send_timer = Timer(30, self._output)
        send_timer.start()
        self._input()

    def _input(self):
        global lock
        for msg in self._consumer:
            try:
                lock.acquire()
                self.data.append(self._decode(msg.value))
            except Exception, e:
                traceback.print_exc()
            finally:
                lock.release()

    def bulk_data(self, data):
        actions = []
        for item in data:
            try:
                idx = "%s_%s" % (self._index, datetime.datetime.now().strftime("%Y%m%d"))
                action = {"_index":idx, "_type":self.topic, "_source":{}}
                for k, v in item.items():
                    action["_source"][k] = v

                actions.append(action)
            except Exception, e:
                traceback.print_exc()

        return actions

    def _output(self):
        global send_timer, lock
        lock.acquire()
        _data = copy.deepcopy(self.data)
        self.data = []
        lock.release()
        try:
            actions = self.bulk_data(_data)
            if actions:
                helpers.bulk(self.es, actions)
        except Exception, e:
            traceback.print_exc()
        finally:
            send_timer = Timer(30, self._output)
            send_timer.start()

if __name__ == "__main__":
    obj = Kafka2ES()
    obj.run()
