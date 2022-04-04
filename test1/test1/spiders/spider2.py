import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from test1.items import Test1Item

class Spider2Spider(CrawlSpider):
    name = 'spider2'
    allowed_domains = ['4399dmw.com']
    start_urls = ['http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/']

    # 决定爬虫的走向，爬到的页面是否需要跟进，到某个页面使用什么函数处理
    rules = (
        Rule(LinkExtractor(allow=r'.+dh-1-0-0-0-0-\d-0\/'),follow=True),
        Rule(LinkExtractor(allow=r'.+\/dh\/.+\/'),callback='parse_detail',follow=False)
    )


    def parse_item(self, response):
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        datas_pic = response.xpath("//a[@class='u-card']/img")
        for item in datas_pic:
            pic = "http:" + str(item.xpath("@data-src")[0].extract())
            title = item.xpath("@alt").extract()
            topipeline1 = Test1Item(pic=pic, title=title)
            yield topipeline1

    def prase_detail(self,response):
        title = response.xpath("//div[@class='works__main']/h1/text()").extract()[0]
        jianjie = response.xpath("//div[@class='main']/div/p/text()").extract()[0]
        pic = "http:" + str(response.xpath("//div[@class='works__main']//img[@class='works__img']/@data-src")[0].extract())
        topipeline2 = Test1Item(jianjie=jianjie,pic=pic,title=title)
        yield topipeline2

        pass