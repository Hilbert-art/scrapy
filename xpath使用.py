import requests
from lxml import etree
import random


def scrapy(url):
    url = url

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers)
    html_doc = resp.content.decode('utf-8')
    html = etree.HTML(html_doc)
    dongman_title = html.xpath("//div[@class='u-ct']/p[@class='u-tt']/text()")
    dongman_pic = html.xpath("//div[@class='lst']/a/img/@data-src")
    print(dongman_title)
    print(dongman_pic)


def find_next_page(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers)
    html_doc = resp.content.decode('utf-8')
    html = etree.HTML(html_doc)
    next_page = html.xpath("//a[contains(text(),'下一页')]/@href")
    really_url = "http://www.4399dmw.com" + next_page[0]
    return really_url


def main():
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/"

    # while True:
    #     try:
    #         scrapy(url)
    #         next_page = find_next_page(url)
    #         url = next_page
    #         print(url)
    #     except:
    #         print("The last page has been done!")
    #         break
    # version_id = random.randint(50,120)
    # os_type = ['Windows NT 10.0','Windows NT 6.1','Linux 10.0']
    # ua = "Mozilla/5.0 ("+random.choice(os_type)+"; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758."+str(version_id)+" Safari/537.36"
    # # ua1 = "".join(["Mozilla/5.0 (",random.choice(os_type),"; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.",str(version_id)," Safari/537.36"])
    referer = f"http://www.4399dmw.com/search/dh-1-0-0-0-0-{random.randint(1, 14)}-0/"
    print(referer)


if __name__ == '__main__':
    main()
