#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from engine import Engine
from downloader import Downloader
from spider import Spider

downloader = Downloader()
spider = Spider()
engine = Engine(downloader, spider)
for i in xrange(1):
    engine.fire(i, str(i) + "eng")
