from scrapy_redis.spiders import RedisCrawlSpider, RedisSpider

from bilibilispider.items import  Little_Area_Heat


# 小分区热度

class JobList(RedisSpider):
    name = 'little_area_heat'
    # allowed_domains = ["www.kanbilibili.com"]
    redis_key = "job:start_url"

    # 循环遍历得到的start——url

    def parse(self, response):
        div_list = response.xpath("//div[@class = 'daily-content all']/div")
        for div in div_list:
            larea_heat_info = Little_Area_Heat()
            larea_heat_info['area'] = response.xpath(
                "//li[@class = 'level1 active']/span/span/span/text()").extract_first()
            larea_heat_info['little_area'] = response.xpath(
                "//li[@class = 'level3 active']/span/text()").extract_first()
            larea_heat_info['name'] = div.xpath(".//span[@class = 'title']/text()").extract_first()
            larea_heat_info['view_time'] = div.xpath(".//div[@class='info total']/span[@class = 'play']/text()").extract_first()
            yield larea_heat_info