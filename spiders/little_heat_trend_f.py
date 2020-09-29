from scrapy_redis.spiders import RedisCrawlSpider, RedisSpider

from bilibilispider.items import  Little_Heat_Trend


# 小分区热度趋势

class JobList(RedisSpider):
    name = 'little_heat_trend'
    # allowed_domains = ["www.kanbilibili.com"]
    redis_key = "job:start_url"

    # 循环遍历得到的start——url

    def parse(self, response):
        div_list = response.xpath("//div[@class = 'daily-content daily']/div")
        for div in div_list:
            larea_heat_info = Little_Heat_Trend()
            larea_heat_info['area'] = response.xpath(
                "//li[@class = 'level1 active']/span/span/span/text()").extract_first()
            larea_heat_info['little_area'] = response.xpath(
                "//li[@class = 'level3 active']/span/text()").extract_first()
            larea_heat_info['name'] = div.xpath(".//span[@class = 'title']/text()").extract_first()
            larea_heat_info['time'] = "20200603"  # 记得修改
            larea_heat_info['view_time'] = div.xpath(".//div[@class='info count']/span[@class = 'play']/text()").extract_first()
            yield larea_heat_info