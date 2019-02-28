#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2
from vndb import DBHelper
from engine import Engine
from downloader import Downloader
from spider import Spider

db_conf = {
    'user': 'vien',
    'passwd': 'vien',
    'host': '127.0.0.1',
    'schema': 'vien',
    'charset': 'utf8mb4',
}


def save_img(url, path):
    f = urllib2.urlopen(url)
    data = f.read()
    with open(path, "wb") as code:
        code.write(data)


def md5(txt):
    import hashlib
    m = hashlib.md5()
    m.update(txt)
    return m.hexdigest()


if __name__ == '__main__':
    with DBHelper(**db_conf) as db:
        urls = db.get_dicts(" SELECT id, img_standard_url FROM ins_meme_tag_data ")
        path = "/Users/vien/img/"
        downloader = Downloader()
        spider = Spider()
        engine = Engine(downloader, spider)
        count = 0
        for url in urls:
            try:
                engine.fire(url['img_standard_url'], url)
            except Exception as e:
                print(e)
                # cur_url = url['img_standard_url']
                # file_name = md5(cur_url) + cur_url[cur_url.rfind('.'):]
                # try:
                #     save_img(cur_url, path + file_name)
                # except Exception as e:
                #     print e
                #     continue
                # row_count = db.execute(" UPDATE ins_meme_tag_data SET img_file_name = %s WHERE id = %s ",
                #                        (file_name, url['id']))
                # count = count + 1
                # print(row_count, file_name, count)
