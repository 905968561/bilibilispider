from scrapy_redis.spiders import RedisCrawlSpider, RedisSpider

from bilibilispider.items import Up_Info


# 爬取粉丝前百的up主简要信息

class JobList(RedisSpider):
    name = 'up_partition'
    # allowed_domains = ["www.kanbilibili.com"]
    redis_key = "job:start_url"

    # 循环遍历得到的start——url

    def parse(self, response):
        a_list = response.xpath("//div[@class='ups-list']/a")
        for a in a_list:
            up_info = Up_Info()
            up_info['area'] = response.xpath("//a[@class = 'blue active']/text()").extract_first()
            up_info['name'] = a.xpath("./div/div[@class = 'basic']/span[@class = 'name blue']/text()").extract_first()
            up_info['fans_num'] = a.xpath(
                "./div/div[@class = 'info']/div[@class ='info-item']/p[@class = 'data fans']/text()").extract_first()
            c = filter(str.isdigit, up_info['fans_num'])
            b = ''.join(c)
            s = int(b) * 100
            if s > 2360000:
                yield up_info
