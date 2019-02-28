#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import hashlib
from vndb import DBHelper

db_conf = {
    'user': 'vien',
    'passwd': 'vien',
    'host': '127.0.0.1',
    'schema': 'vien',
    'charset': 'utf8mb4',
}


class Spider(object):
    def parse(self, response):
        resp = response.get_response()
        if resp:
            url = response.get_item()
            cur_url = url['img_standard_url']
            file_name = self.md5(cur_url) + cur_url[cur_url.rfind('.'):]
            path = "/Users/vien/img/"

            with open(path + file_name, 'wb') as f:
                f.write(resp.content)
            with DBHelper(**db_conf) as db:
                row_count = db.execute(" UPDATE ins_meme_tag_data SET img_file_name = %s WHERE id = %s ",
                                       (file_name, url['id']))
                print(row_count, file_name, url['id'])

    def md5(self, s):
        m = hashlib.md5()
        m.update(str(s))
        return m.hexdigest()
