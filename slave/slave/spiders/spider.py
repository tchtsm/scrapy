import re
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from slave.items import SlaveItem

class myspider(RedisSpider):
    name = 'slave'
    item = SlaveItem()
    redis_key = 'myredis:start_urls'

    def parse(self, response):
        item = self.item
        item['title'] = response.xpath('//div[@class="house-title"]/h1/text()').extract()[0]
        item['price'] = response.xpath('//div[@id="generalSituation"]//li[1]/span[2]/text()').extract()[0]
        item['type'] = response.xpath("//div[@id='generalSituation']//li[2]/span[2]/text()").extract()[0]
        item['area'] = response.xpath("//div[@id='generalSituation']//li[3]/span[2]/text()").extract()[0]
        item['direct'] = response.xpath("//div[@id='generalSituation']//li[4]/span[2]/text()").extract()[0]
        item['floor'] = response.xpath(
            "//div[@id='generalSituation']//ul[@class='general-item-right']/li[1]/span[2]/text()").extract()[0]
        item['decorat'] = response.xpath(
            "//div[@id='generalSituation']//ul[@class='general-item-right']/li[2]/span[2]/text()").extract()[0]
        item['start'] = response.xpath(
            "//div[@id='generalSituation']//ul[@class='general-item-right']/li[4]/span[2]/text()").extract()[0]
        item['village'] = response.xpath("string(/html/body/div[4]/div[2]/div[2]/ul/li[1]/span[2])").extract()[0]
        item['position'] = response.xpath("string(/html/body/div[4]/div[2]/div[2]/ul/li[2]/span[2])").extract()[0]
        item['phone'] = response.xpath("//div[@id='houseChatEntry']//p[@class='phone-num']/text()").extract()[0]
        txt = response.xpath("/html/head/script[1]/text()").extract()[0]
        pattern = re.compile(".*?____json4fe.brokerUrl = '(.*?)';.*?", re.S)
        result = re.findall(pattern, txt)
        yield Request("http://" + result[0], callback=self.get_user)

    def get_user(self, response):
        item = self.item
        item['user'] = response.xpath("/html/body/div[2]/div[2]/div[1]/div[1]/div/div[1]/text()").extract()[0]
        return item