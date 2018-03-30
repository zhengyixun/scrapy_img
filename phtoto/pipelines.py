# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from settings import IMAGES_STORE as image_store
from scrapy.pipelines.images import ImagesPipeline

class PhtotoPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):

        imgurl = item['imgurl']
        yield scrapy.Request(imgurl)
    #     s设置item相关信息 重新设置path和图片名
    def item_completed(self, results, item, info):
        imgpath = [x['path'] for ok, x in results if ok]
        os.rename(image_store + imgpath[0], image_store + item['nickname'] + ".jpg")
        return item