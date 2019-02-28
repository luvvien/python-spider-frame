#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Request(object):
    """docstring for Request"""

    def __init__(self, key, url, call, item=None):
        self._key = key
        self._url = url
        self._call = call
        self._item = item

    def get_key(self):
        return self._key

    def get_url(self):
        return self._url

    def get_call(self):
        return self._call

    def get_item(self):
        return self._item
