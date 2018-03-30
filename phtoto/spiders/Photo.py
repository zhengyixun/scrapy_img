# -*- coding: utf-8 -*-
import scrapy
from phtoto.items import PhtotoItem
import json
class PhotoSpider(scrapy.Spider):
    name = 'Photo'
    # allowed_domains = [''user.qzone.com'']

    baseurl = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [baseurl + str(offset)]
    def parse(self, response):
        data = json.loads(response.body)['data']
        if not len(data):
            return
        for d in data:
            item = PhtotoItem()
            item['nickname'] = d['nickname']
            item['imgurl'] = d['vertical_src']
            yield item
        # 下载所有
        # self.offset += 20
        # scrapy.Request(self.baseurl + str(self.offset))
