# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibilispiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 必要
class User_Info(scrapy.Item):
    uid = scrapy.Field()
    name = scrapy.Field()
    space = scrapy.Field()
    sex = scrapy.Field()
    birthday = scrapy.Field()
    address = scrapy.Field()
    level = scrapy.Field()


# 必要
class Up_Info(scrapy.Item):
    area = scrapy.Field()
    name = scrapy.Field()
    fans_num = scrapy.Field()


# 必要
class Area_Heat(scrapy.Item):
    area = scrapy.Field()
    name = scrapy.Field()
    view_time = scrapy.Field()


# 必要
class Little_Area_Heat(scrapy.Item):
    area = scrapy.Field()
    little_area = scrapy.Field()
    name = scrapy.Field()
    view_time = scrapy.Field()


# 必要
class Heat_Trend(scrapy.Item):
    area = scrapy.Field()
    name = scrapy.Field()
    time = scrapy.Field()
    view_time = scrapy.Field()


# 必要
class Little_Heat_Trend(scrapy.Item):
    area = scrapy.Field()
    little_area = scrapy.Field()
    name = scrapy.Field()
    time = scrapy.Field()
    view_time = scrapy.Field()
