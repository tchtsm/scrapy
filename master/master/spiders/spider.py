from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from master.items import MasterItem

class myspider(CrawlSpider):

    name = 'master'
    allowed_domains = ['58.com']
    item = MasterItem()
    start_urls = ['http://cd.58.com/ershoufang/']
    rules = (
        Rule(LinkExtractor(allow=('http://cd.58.com/ershoufang/\d{14}x.shtml.*?',)), callback='parse_item',
             follow=True),
    )

    def parse_item(self,response):
        item = self.item
        item['url'] = response.url
        return item