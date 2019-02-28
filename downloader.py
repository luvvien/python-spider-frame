#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import random
import requests
from socket import error as SocketError
from concurrent.futures import ThreadPoolExecutor

import conf
from response import Response


class Downloader(object):
    def __init__(self):
        self._pool = ThreadPoolExecutor(max_workers=conf.MAX_THREAD_SIZE)

    def submit(self, req):
        self._pool.submit(self._throw2pool, req)

    def _throw2pool(self, req):
        url = req.get_url()
        key = req.get_key()
        func = req.get_call()
        res = dict()
        res["key"] = key
        try:
            response = self._get_res_by_url(url)
            res["value"] = Response(url, response, req.get_item())
            func(res)
        except Exception as e:
            print(e)
            res["value"] = Response(url, None, req.get_item())
            func(res)
            raise e



    # def _get_res_by_url(self, url):
    #     time.sleep(random.randint(1, 3))
    #     return str(url) + 'response'

    def _get_res_by_url(self, url):
        count = 0
        res = None
        while True:
            try:
                res = requests.get(url)
                break
            except SocketError as e:
                if count > 5:
                    raise e
                print(e, 'Try again!')
                count = count + 1
                time.sleep(1)
        return res
