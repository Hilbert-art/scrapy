import scrapy
from test1.items import Test1Item


class Spider1Spider(scrapy.Spider):
    # 爬虫根据这个名字运行
    name = 'spider1'
    # 允许的域名
    allowed_domains = ['4399dmw.com']
    # 从什么域名开始
    start_urls = ['http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/']

    def parse(self, response):
        # 图片地址//a[@class='u-card']/img/@src
        # 文字地址//a[@class='u-card']/img/@alt
        datas_pic = response.xpath("//a[@class='u-card']/img")
        for item in datas_pic:
            pic = "http:"+str(item.xpath("@data-src")[0].extract())
            title = item.xpath("@alt").extract()
            topipeline1 = Test1Item(pic=pic,title=title)
            yield topipeline1


