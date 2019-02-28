#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class Response(object):
    def __init__(self, url, response=None, item=None):
        self._url = url
        self._response = response
        self._item = item

    def set_url(self, url):
        self._url = url

    def get_url(self):
        return self._url

    def set_response(self, response):
        self._response = response

    def get_response(self):
        return self._response

    def set_item(self, item):
        self._item = item

    def get_item(self):
        return self._item