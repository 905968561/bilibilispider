import json

import scrapy
from scrapy import FormRequest

from bilibilispider.items import User_Info


class User_Link(scrapy.Spider):
    name = 'user_info'

    def start_requests(self):
        sourse = "https://api.bilibili.com/x/relation/followers?vmid=546195&pn={}&ps=100&order=desc&jsonp=jsonp"
        for i in range(5):
            url = sourse.format(i + 1)
            yield FormRequest(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        users = json.loads(response.text)
        all_list = users['data']['list']
        for list in all_list:
            mid = list['mid']
            url = 'https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'.format(mid)
            yield FormRequest(url, callback=self.parse_up, dont_filter=True)

    def parse_up(self, response):
        user = json.loads(response.text)
        user = user['data']
        item = User_Info()
        item['uid'] = user['mid']
        item['name'] = user['name']
        item['space'] = 'https://space.bilibili.com/' + str(item['uid'])
        item['sex'] = user['sex']
        try:
            item['birthday'] = user['birthday']
        except KeyError:
            item['birthday'] = ''
        try:
            item['address'] = user['place']
        except KeyError:
            item['address'] = ''
        item['level'] = user['level']
        yield item
