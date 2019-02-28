#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
from Queue import Queue
from threading import Thread

import conf
from request import Request
from downloader import Downloader
from spider import Spider


class Engine(object):
    def __init__(self, downloader, spider=None):
        self._counter = 0
        # self._end_flag = 0
        # self._request_queue = Queue(conf.REQUEST_QUEUE_MAXSIZE)
        # self._response_queue = Queue(0)
        self._order_record_queue = Queue(conf.REQUEST_QUEUE_MAXSIZE)
        self._result_pool = dict()
        self._downloader = downloader
        self._spider = spider
        listener = Thread(target=self._listen_result_pool)
        listener.setDaemon(True)
        listener.start()

    def _package_request_obj2queue(self, url, item=None):
        key = self._counter
        self._counter = self._counter + 1
        req = Request(key, url, self._put_result2result_pool_callback, item)
        # self._request_queue.put(req)
        self._order_record_queue.put(key)
        return req

    def _submit_request2downloader(self, req):
        self._downloader.submit(req)

    def _put_result2result_pool_callback(self, result):
        self._result_pool[result["key"]] = result["value"]

    def _listen_result_pool(self):
        while 1:
            if self._order_record_queue.empty():
                # self._end_flag = 1
                continue
            # else:
            #     self._end_flag = 0
            cur_key = self._order_record_queue.get()
            while 1:
                if cur_key in self._result_pool:
                    self._spider.parse(self._result_pool[cur_key])
                    break
                else:
                    continue

    def fire(self, url, item=None):
        req = self._package_request_obj2queue(url, item)
        self._submit_request2downloader(req)

        # def fire(self):
        #     for i in xrange(10):
        #         self._package_request_obj2queue(i)
        #     for i in xrange(10):
        #         req = self._request_queue.get()
        #         self._submit_request2downloader(req)
        #         print "fire"
        #     listener = Thread(target=self._listen_result_pool)
        #     listener.setDaemon(True)
        #     listener.start()

        #     for i in xrange(10):
        #         print self._response_queue.get()


if __name__ == '__main__':
    downloader = Downloader()
    spider = Spider()
    engine = Engine(downloader, spider)
    for i in xrange(30):
        engine.fire(i, str(i) + "item")
