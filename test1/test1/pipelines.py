# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os
from urllib import request
from test1 import settings
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class Test1Pipeline:
    # 打开爬虫的时候执行
    def open_spider(self, spider):
        # 打开并准备存储
        self.fp = open("spider1.json", "w", encoding='utf-8')
        # 判断路径是否存在，当前目录下是否有文件夹，没有就创建一个
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    # 使用yield时候执行
    def process_item(self, item, spider):
        item_json = json.dumps(dict(item), ensure_ascii=False)
        # item_json = json.dumps(item,ensure_ascii=False)
        self.fp.write(item_json + '\n')
        # 获得item的细节
        title = item['title'][0]
        pic = item['pic']
        path1 = os.path.join(self.path, 'pic1')
        if not os.path.exists(path1):
            os.mkdir(path1)
        # 下载图片并且加上jpg后缀
        request.urlretrieve(pic, os.path.join(path1, title + '.jpg'))
        return item

    # 爬虫结束时候执行
    def close_spider(self, spider):
        # 结束关闭文件
        self.fp.close()


# 重写图片下载类
class newImagePipeline(ImagesPipeline):
    # 请求之前调用
    def get_media_requests(self, item, info):
        for image_url in item['pic']:
            yield Request(image_url)

    # 请求之后调用
    def file_downloaded(self, response, request, info, *, item=None):
        # 重写path方法
        path = super(newImagePipeline, self).file_path(request, response, info)
        # 获得图片类型以新建文件夹
        category = request.item.get('category')
        # 获得settings里的图片的路径
        image_store = settings.IMAGE_STORE
        category_path = os.path.join(image_store, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        # 修改原有图片的名字
        image_name = path.replace("full/", "")
        # 真正图片的路径
        image_path = os.path.join(category_path, image_name)
        return image_path
