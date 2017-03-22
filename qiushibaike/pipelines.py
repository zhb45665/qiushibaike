# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class QiushibaikePipeline(object):
    def __init__(self, sqlite_file, sqlite_table):
        self.sqlite_file = sqlite_file
        self.sqlite_table = sqlite_table
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_file = crawler.settings.get('SQLITE_FILE'), # 从 settings.py 提取
            sqlite_table = crawler.settings.get('SQLITE_TABLE')
        )
    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.cur = self.conn.cursor()
    def process_item(self, item, spider):
        insertsql = "insert into %s (content,auther) values (\'%s\',\'%s\')" % (self.sqlite_table,item['content'][0],item['auther'][0])
        self.cur.execute(insertsql)
        self.conn.commit()
        return item
    def close_spider(self, spider):
        self.conn.close