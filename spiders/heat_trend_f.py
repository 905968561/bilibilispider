from scrapy_redis.spiders import RedisCrawlSpider, RedisSpider

from bilibilispider.items import Heat_Trend


# 分区热度趋势

class JobList(RedisSpider):
    name = 'heat_trend'
    # allowed_domains = ["www.kanbilibili.com"]
    redis_key = "job:start_url"

    # 循环遍历得到的start——url

    def parse(self, response):
        div_list = response.xpath("//div[@class = 'daily-content daily']/div")
        for div in div_list:
            area_heat_info = Heat_Trend()
            area_heat_info['area'] = response.xpath(
                "//li[@class = 'level1 active']/span/span/span/text()").extract_first()
            area_heat_info['name'] = div.xpath(".//span[@class = 'title']/text()").extract_first()
            area_heat_info['time'] = "20200603"  # 记得修改
            area_heat_info['view_time'] = div.xpath(
                ".//div[@class='info count']/span[@class = 'play']/text()").extract_first()
            yield area_heat_info
