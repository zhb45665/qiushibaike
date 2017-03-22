# -*- coding: utf-8 -*-
import scrapy
import sqlite3
from qiushibaike.items import QiushibaikeItem
from scrapy.settings.default_settings import DOWNLOAD_DELAY
from scrapy.http import Request
from scrapy.item import Item

class QiushiSpider(scrapy.Spider):
    DOWNLOAD_DELAY = 1
    name = "qiushi"
    allowed_domains = ["www.qiushibaike.com"]
    start_urls = ['http://www.qiushibaike.com/text/',
                  'http://www.qiushibaike.com/history/',
                  'http://www.qiushibaike.com/textnew/',
                  'http://www.qiushibaike.com/',
                  'http://www.qiushibaike.com/hot/']
    def parse(self, response):
#     	for sel in response.xpath('//div[@class="content"]'):
#     		item = QiushibaikeItem()
#     		item['span'] = sel.xpath('span/text()').extract()
#     		yield item
#     	for auth in response.xpath('//div[@class="author clearfix"]'):
#     		item = QiushibaikeItem()
#     		item['auth'] = auth.xpath('a/h2/text()').extract()
#     		yield item
#         sel = Selector(response)
        items = response.xpath('//div[@class="article block untagged mb15"]')
        links = response.xpath('//ul[@class="pagination"]/li/a/span[@class="next"]/../@href').extract()
        item = QiushibaikeItem()
        for url in links:
            ur = 'http://www.qiushibaike.com' + url
            for co in items:
                item['auther'] = co.xpath('div/a/h2/text()').extract()
                item['content'] = co.xpath('a/div/span/text()').extract()
                yield item
            if url == '/hot/':
                continue
            if url == '/week/':
                continue
            yield Request(ur, callback=self.parse)
        return item
#       filename = response.url.split("/")[-2]
#      with open(filename,'wb') as f:
#      	f.write(response.body)


